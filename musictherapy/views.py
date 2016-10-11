from collections import namedtuple, defaultdict
from datetime import datetime

import django.contrib.auth.views as auth
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_GET

import musictherapy.models as models
from musictherapy.forms import *
from musictherapy.skills_data import SkillsData

STATUS_MESSAGES = {
    'no_permission': 'You do not have permission to use this function.  Talk to an administrator if you have further questions.',
    'pass_change_success': 'Password changed successfully.',
    'staff_added': 'Staff member added successfully.'
}

PREFIXES = {
    'general': 'General',
    'com': 'Communication',
    'pss': 'Psycho-Social',
    'physical': 'Physical',
    'cog': 'Cognitive',
    'music': 'Music',
    'affective': 'Affective',
    'gen': 'General',
    'psy': 'Psycho-Social',
    'phy': 'Physical',
    'mus': 'Music',
    'aff': 'Affective',
}


def index(request):
    if request.user.is_authenticated():
        return redirect('/musictherapy/patients')
    else:
        return render(request, 'musictherapy/index.html', {
            'form': AuthenticationForm(request=request),
            'next': '/musictherapy/patients'
        })


def login(request):
    return auth.login(request)


@require_GET
@login_required(login_url='/musictherapy/login')
def patients(request):
    status = request.GET.get('status', None)
    user_info_list = models.UserInfo.objects.all().order_by('location')
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/patients.html', context)


@login_required(login_url='/musictherapy/login')
def user_detail(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    user_form = UserInfoForm(instance=user)
    user_last_updated = user.updated

    program_form = ProgramForm()

    musicpref = get_object_or_None(models.MusicalPreference, pk=user_id)
    musicpref_form = MusicalPrefForm(instance=musicpref)
    musicpref_last_updated = musicpref.updated if musicpref else None

    com = SkillsData("Communication", user)
    pss = SkillsData("Psycho-Social", user)
    physical = SkillsData("Physical", user)
    cog = SkillsData("Cognitive", user)
    music = SkillsData("Music", user)
    affective = SkillsData("Affective", user)

    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'goals': get_goals(user),
        'session_goals': {data.domain: data.goals_measurables() for data in [com, pss, physical, cog, music, affective]},
        'user_last_updated': user_last_updated,
        'program_form': program_form,

        'summary': {data.domain: data.summary_measurable() for data in [com, pss, physical, cog, music, affective]},

        'musical_pref_form': musicpref_form,
        'musicpref_last_updated': musicpref_last_updated,

        'general_goals': SkillsData("General", user).to_dict(),
        'com_data': com.to_dict(),
        'pss_data': pss.to_dict(),
        'physical_data': physical.to_dict(),
        'cog_data': cog.to_dict(),
        'music_data': music.to_dict(),
        'affective_data': affective.to_dict(),
    })


@login_required(login_url='/musictherapy/login')
def create_user(request):
    user_form = UserInfoForm()
    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'new': True
    })


@login_required(login_url='/musictherapy/login')
def save_program(request):
    if request.method == 'POST':
        program_form = ProgramForm(request.POST)
        print(program_form.is_valid())
        if program_form.is_valid():
            program = program_form.save()
            return redirect('musictherapy/')
    return HttpResponse(404)


@login_required(login_url='/musictherapy/login')
def save_new_basic(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('/musictherapy/' + str(user.pk), {
                'tab': 'user_info',
            })
        else:
            print("From was not valid")
            return HttpResponse(404)


@permission_required(perm='musictherapy.delete_userinfo')
@login_required(login_url='/musictherapy/login')
def delete_user(request, user_id):
    if request.user.has_perm('muscitherapy.userinfo.can_delete'):
        user = get_object_or_404(models.UserInfo, pk=user_id)
        user.delete()
        return redirect('/musictherapy/')
    else:
        return redirect('/musictherapy/patients?status=no_permission')


@login_required(login_url='/musictherapy/login')
def save_user_goals(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    user_goals = [ug.pk for ug in models.UserGoals.objects.filter(user=user)]
    if request.method == 'POST':
        for goal in request.POST.getlist('goals', []):
            goal_model = models.Goals.objects.get(pk=goal)
            user_goal = get_object_or_None(models.UserGoals, goal=goal_model)
            if not user_goal:
                user_goal = models.UserGoals(user=user, goal=goal_model)
                user_goal.save()
            else:
                user_goals.remove(user_goal.pk) if user_goal.pk in user_goals else None

        for ug in user_goals:
            models.UserGoals.objects.get(pk=ug).delete()
        return redirect('/musictherapy/' + user_id)


@permission_required(perm='auth.add_user')
@require_http_methods(["GET", "POST"])
@login_required(login_url='/musictherapy/login')
def create_staff(request):
    if request.method == 'GET':
        context = {
            'staff_form': StaffForm()
        }
        return render(request, 'musictherapy/staff.html', context)
    elif request.method == 'POST':
        staff_form = StaffForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            return redirect('/musictherapy/patients?status=staff_added')
        else:
            return render(request, 'musictherapy/staff.html', {
                'staff_form': staff_form,
            })


@login_required(login_url='/musictherapy/login')
def save_basic_info(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def save_music_pref(request, user_id):
    musicpref = get_object_or_None(models.MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = MusicalPrefForm(request.POST, instance=musicpref)
        if musicpref_form.is_valid():
            if musicpref is None:
                musicpref = musicpref_form.save(commit=False)
                musicpref.user = get_object_or_404(models.UserInfo, pk=user_id)
            musicpref_form.save()
            return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def save_measurables(request, user_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        date = datetime.now()
        for measurable_id, measurable_value in data.iteritems():
            if measurable_id.lower() in ['save', 'csrfmiddlewaretoken', 'submit', 'redirect']:
                continue

            elif 'measurablesnotes' in measurable_id.lower():
                domain_prefix = measurable_id.lower().split('_')[0]
                domain = get_object_or_404(models.Domains, name=PREFIXES[domain_prefix])
                notes = models.UserDomainNoteMeasurables(user=user, domain=domain, note=measurable_value, updated=date)
                notes.save()

            else:
                measurable = models.DomainMeasurables.objects.get(pk=measurable_id)
                user_measurable = models.UserMeasurables(user=user, measurable=measurable, value=measurable_value, updated=date)
                user_measurable.save()

        return redirect('/musictherapy/' + user_id + data['redirect'].lower())


@login_required(login_url='/musictherapy/login')
def save_goalmeasurables(request, user_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        date = datetime.now()
        for measurable_id, measurable_value in data.iteritems():
            if measurable_id.lower() in ['save', 'csrfmiddlewaretoken', 'submit', 'redirect']:
                continue

            elif 'goalsnotes' in measurable_id.lower():
                domain_prefix = measurable_id.lower().split('_')[0]
                domain = get_object_or_404(models.Domains, name=PREFIXES[domain_prefix])
                notes = models.UserGoalNoteMeasurable(user=user, domain=domain, note=measurable_value, updated=date)
                notes.save()

            else:
                measurable = models.GoalsMeasurables.objects.get(pk=measurable_id)
                user_measurable = models.UserGoalMeasurables(user=user, goal_measurable=measurable, value=measurable_value, updated=date)
                user_measurable.save()

        return redirect('/musictherapy/' + user_id + data['redirect'].lower())


def get_goals(user):
    goals = defaultdict(list)
    for g in models.Goals.objects.filter(parent=None, enabled=1).order_by('domain'):
        goals[g.domain.name if g.domain.parent is None else g.domain.parent.name] += [g]
    goals = dict(goals)
    goals['order'] = ['General'] + [domain for domain in goals.keys() if domain != 'General']
    goals['user'] = [ug.goal.pk for ug in models.UserGoals.objects.filter(user=user)]
    return goals