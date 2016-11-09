import json
from collections import defaultdict
from datetime import datetime

import django.contrib.auth.views as auth
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_GET

from musictherapy.forms import *
from musictherapy.goals import get_session_goals, get_skills_data_for_user_as_list
from musictherapy.sessions import get_all_sessions, get_current_session
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
        return redirect('/musictherapy/users')
    else:
        return render(request, 'musictherapy/index.html', {
            'form': AuthenticationForm(request=request),
            'next': '/musictherapy/users'
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
    musicpref_form = MusicalPrefForm(instance=musicpref, user_id=user_id)
    musicpref_last_updated = musicpref.updated if musicpref else None

    sessions = get_all_sessions(user)
    current_session = get_current_session(user)

    goals = get_goals(current_session)
    com = SkillsData("Communication", user)
    pss = SkillsData("Psycho-Social", user)
    physical = SkillsData("Physical", user)
    cog = SkillsData("Cognitive", user)
    music = SkillsData("Music", user)
    affective = SkillsData("Affective", user)
    session_goals = get_session_goals(current_session, user)

    return render(request, 'musictherapy/user_detail.html', {
        # general user details, not session based
        'userinfo': user,
        'user_info_form': user_form,
        'user_last_updated': user_last_updated,
        'program_form': program_form,
        'sessions': sessions,
        'musical_pref_form': musicpref_form,
        'musicpref_last_updated': musicpref_last_updated,

        # session based use details
        'current_session': current_session,
        'goals': goals,
        'session_goals': session_goals,
        'summary': {data.domain: data.summary_measurable() for data in [com, pss, physical, cog, music, affective]},
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
    program_form = ProgramForm()
    return render(request, 'musictherapy/user_detail.html', {
        'user_info_form': user_form,
        'program_form': program_form,
        'new': True
    })


@login_required(login_url='/musictherapy/login')
def save_program(request):
    if request.method == 'POST':
        program_form = ProgramForm(request.POST)
        if program_form.is_valid():
            program = program_form.save()
            serialized = serializers.serialize('json', [program])
            data = json.loads(serialized)
            data = data[0]
            data['display'] = str(program)
            return HttpResponse(json.dumps(data))
        else:
            print(program_form.errors)
    return HttpResponse(404)


@login_required(login_url='/musictherapy/login')
def save_new_basic(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user.pk)}))
        return HttpResponse(user_form.errors)
    return HttpResponse(404)


@login_required(login_url='/musictherapy/login')
def save_basic_info(request, user_id):
    user = get_object_or_None(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}))
        return HttpResponse(user_form.errors)
    return HttpResponse(404)


@permission_required(perm='musictherapy.delete_userinfo')
@login_required(login_url='/musictherapy/login')
def delete_user(request, user_id):
    if request.user.has_perm('muscitherapy.userinfo.can_delete'):
        user = get_object_or_404(models.UserInfo, pk=user_id)
        user.delete()
        return redirect('/musictherapy/')
    else:
        return redirect('/musictherapy/users?status=no_permission')


@login_required(login_url='/musictherapy/login')
def save_user_goals(request, user_id):
    print(user_id)
    user = get_object_or_404(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        session = get_object_or_None(models.Session, pk=request.POST.get('session'))
        if not session:
            session = models.Session(user=user)
            session.save()
        user_goals = [ug.pk for ug in models.UserGoals.objects.filter(session=session)]
        for goal in request.POST.getlist('goals', []):
            goal_model = models.Goals.objects.get(pk=goal)
            user_goal = get_object_or_None(models.UserGoals, goal=goal_model, session=session)
            if not user_goal:
                user_goal = models.UserGoals(session=session, goal=goal_model)
                user_goal.save()
            else:
                user_goals.remove(user_goal.pk) if user_goal.pk in user_goals else None

        for ug in user_goals:
            models.UserGoals.objects.get(pk=ug).delete()
    print(user_id)
    return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}))


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
            return redirect('/musictherapy/users?status=staff_added')
        else:
            return render(request, 'musictherapy/staff.html', {
                'staff_form': staff_form,
            })


@login_required(login_url='/musictherapy/login')
def save_music_pref(request, user_id):
    musicpref = get_object_or_None(models.MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = MusicalPrefForm(request.POST, instance=musicpref, user_id=user_id)
        if musicpref_form.is_valid():
            if musicpref is None:
                musicpref = musicpref_form.save(commit=False)
                musicpref.user = get_object_or_404(models.UserInfo, pk=user_id)
            musicpref_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}))


@login_required(login_url='/musictherapy/login')
def save_measurables(request, user_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        d = datetime.now()
        for measurable_id, measurable_value in data.iteritems():
            if measurable_id.lower() in ['save', 'csrfmiddlewaretoken', 'submit', 'redirect']:
                continue

            elif 'measurablesnotes' in measurable_id.lower():
                domain_prefix = measurable_id.lower().split('_')[0]
                domain = get_object_or_404(models.Domains, name=PREFIXES[domain_prefix])
                notes = models.UserDomainNoteMeasurables(user=user, domain=domain, note=measurable_value, updated=d)
                notes.save()

            else:
                measurable = models.DomainMeasurables.objects.get(pk=measurable_id)
                user_measurable = models.UserMeasurables(user=user, measurable=measurable, value=measurable_value, updated=d)
                user_measurable.save()

        return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}))


@login_required(login_url='/musictherapy/login')
def save_goalmeasurables(request, user_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        session = get_object_or_None(models.Session, pk=data['session'])
        if not session:
            session = models.Session(user=user)
            session.save()

        for measurable_id, measurable_value in data.iteritems():
            if measurable_id.lower() in ['save', 'csrfmiddlewaretoken', 'submit', 'redirect', 'session']:
                continue

            elif 'goalsnotes' in measurable_id.lower():
                domain_prefix = measurable_id.lower().split('_')[0]
                domain = get_object_or_404(models.Domains, name=PREFIXES[domain_prefix])
                notes = get_object_or_None(models.UserGoalNoteMeasurable, session=session, domain=domain)
                if not notes:
                    notes = models.UserGoalNoteMeasurable(session=session, domain=domain, note=measurable_value)
                else:
                    notes.note = measurable_value
                notes.save()

            else:
                measurable = models.GoalsMeasurables.objects.get(pk=measurable_id)
                user_measurable = models.UserGoalMeasurables(session=session, goal_measurable=measurable, value=measurable_value)
                user_measurable.save()

        if 'redirect' in data:
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id':int(user_id)}))
        return HttpResponse(200)
    return HttpResponse(404)


def get_goals(session):
    goals = defaultdict(list)
    for g in models.Goals.objects.filter(parent=None, enabled=1).order_by('domain'):
        goals[g.domain.name if g.domain.parent is None else g.domain.parent.name] += [g]
    goals = dict(goals)
    goals['order'] = ['General'] + [domain for domain in goals.keys() if domain != 'General']
    goals['user'] = [ug.goal.pk for ug in models.UserGoals.objects.filter(session=session)]
    return goals


@login_required(login_url='/musictherapy/login')
def program_detail(request, program_id):
    program = get_object_or_None(models.Program, pk=program_id)
    users = models.UserInfo.objects.filter(program=program)

    session_goals = {}
    for user in users:
        session_goals[user.pk] = {data.domain: data.goals_measurables() for data in get_skills_data_for_user_as_list(user)}

    return render(request, 'musictherapy/program_details.html', {
        'program': program,
        'users': users,
        'session_goals': session_goals,
    })

