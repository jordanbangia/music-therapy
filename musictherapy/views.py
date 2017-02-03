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
from musictherapy.goals import get_session_goals, get_skills_data_for_user_as_list, get_custom_goals
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
        return render(request, 'musictherapy/login.html', {
            'form': AuthenticationForm(request=request),
            'next': '/musictherapy/users'
        })


def login(request):
    return auth.login(request)


@require_GET
@login_required(login_url='/musictherapy/login')
def patients(request):
    status = request.GET.get('status', None)
    user_info_list = models.UserInfo.objects.all().filter(active=1).order_by('location')
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/patients.html', context)


@login_required(login_url='/musictherapy/login')
def all_users(request):
    status = request.GET.get('status', None)
    user_info_list = models.UserInfo.objects.all().order_by('location')
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/base/all_users.html', context)


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

    goals = get_goals(current_session, user)
    com = SkillsData("Communication", user)
    pss = SkillsData("Psycho-Social", user)
    physical = SkillsData("Physical", user)
    cog = SkillsData("Cognitive", user)
    music = SkillsData("Music", user)
    affective = SkillsData("Affective", user)
    session_goals = get_session_goals(current_session, user)
    custom_session_goals = get_custom_goals(current_session, user)

    return render(request, 'musictherapy/user_detail.html', {
        # general user details, not session based
        'userinfo': user,
        'user_info_form': user_form,
        'user_last_updated': user_last_updated,
        'program_form': program_form,
        'sessions': sessions,
        'musical_pref_form': musicpref_form,
        'musicpref_last_updated': musicpref_last_updated,
        'tab': request.GET.get('tab', 'info'),

        # session based use details
        'current_session': current_session,
        'goals': goals,
        'session_goals': session_goals,
        'custom_session_goals': custom_session_goals,
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
        'tab': 'info',
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
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user.pk)}) + "?tab=info")
        return HttpResponse(user_form.errors)
    return HttpResponse(404)


@login_required(login_url='/musictherapy/login')
def save_basic_info(request, user_id):
    user = get_object_or_None(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab=info")
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
    user = get_object_or_404(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        session = None
        session_id = request.POST.get('session', None)
        if session_id and session_id != '':
            session = get_object_or_None(models.Session, pk=session_id)
        if not session:
            session = get_current_session(user)
        user_goals = [ug.pk for ug in models.UserGoals.objects.filter(session=session)]
        custom_goals = [(key, value) for key, value in request.POST.iteritems() if 'custom' in key]

        for domain_key, goal_name in custom_goals:
            if goal_name == '':
                continue

            domain = domain_key.split('_')[0]
            domain = get_object_or_None(models.Domains, name=domain)
            if not domain:
                print("Can't find domain or {}, unable to save custom goal {}".format(domain_key, goal_name))
                continue
            goal = get_object_or_None(models.Goals, name=goal_name, user=user, is_custom=1, enabled=1, domain=domain)
            if not goal:
                goal = models.Goals(name=goal_name, enabled=1, is_custom=1, user=user, domain=domain)
                goal.save()
            user_goal = models.UserGoals(session=session, goal=goal, user=user)
            user_goal.save()

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

        red = request.POST.get('redirect')
        if red == 'program':
            return redirect(reverse('musictherapy:program_detail', kwargs={'program_id': int(user.program.pk)}))
        else:
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab=goals")
    return HttpResponse(404)


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
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab=musicpref")


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

        red = data.get('redirect')
        if red:
            red = red[:3]
        else:
            red = 'info'
        return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab={}".format(red))


@login_required(login_url='/musictherapy/login')
def save_goalmeasurables(request, user_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        session = None
        session_id = request.POST.get('session', None)
        if session_id and session_id != '':
            session = get_object_or_None(models.Session, pk=session_id)
        if not session:
            session = get_current_session(user)

        custom_gm = defaultdict(dict)

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

            elif 'custom' in measurable_id.lower():
                customtag, goal = measurable_id.lower().split('_')
                tag = 'text' if 'text' in customtag else 'value'
                custom_gm[goal][tag] = measurable_value

            else:
                measurable = models.GoalsMeasurables.objects.get(pk=measurable_id)
                user_measurable = models.UserGoalMeasurables(session=session, goal_measurable=measurable, value=measurable_value)
                user_measurable.save()

        for goal_id, measurable in custom_gm.iteritems():
            if 'text' in measurable and measurable['text'] != '':
                goal = get_object_or_None(models.Goals, pk=goal_id)
                if not goal:
                    return HttpResponse(404)
                gm = models.GoalsMeasurables(goal=goal, name=measurable['text'], enabled=1, is_custom=1, user=user)
                gm.save()
                user_measurable = models.UserGoalMeasurables(session=session, goal_measurable=gm, value=measurable['value'])
                user_measurable.save()

        red = data.get('redirect')
        if red:
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab={}".format(red[:3]))
        return HttpResponse(200)
    return HttpResponse(404)


def get_goals(session, user):
    goals = defaultdict(list)
    for g in models.Goals.objects.filter(parent=None, enabled=1).order_by('domain'):
        if g.domain:
            if not g.is_custom or (g.is_custom and g.user == user):
                goals[g.domain.name if g.domain.parent is None else g.domain.parent.name] += [g]
    goals = dict(goals)
    goals['order'] = ['General'] + [domain for domain in goals.keys() if domain not in ('General', 'Custom')]
    if 'Custom' in goals:
        goals['order'] += ['Custom']
    goals['user'] = [ug.goal.pk for ug in models.UserGoals.objects.filter(session=session)]
    return goals


@login_required(login_url='/musictherapy/login')
def program_detail(request, program_id):
    program = get_object_or_None(models.Program, pk=program_id)
    users = models.UserInfo.objects.filter(program=program, active=1)

    session_goals = {}
    goals = {}
    custom_session_goals = {}
    for user in users:
        session_goals[user.pk] = {data.domain: data.goals_measurables(get_current_session(user)) for data in get_skills_data_for_user_as_list(user)}
        goals[user.pk] = get_goals(get_current_session(user), user)
        custom_session_goals[user.pk] = {data.domain: data.custom_goals(get_current_session(user)) for data in get_skills_data_for_user_as_list(user)}

    return render(request, 'musictherapy/program_details.html', {
        'program': program,
        'users': users,
        'session_goals': session_goals,
        'custom_session_goals': custom_session_goals,
        'goals': goals
    })


@login_required(login_url='/musictherapy/login')
def archive_user(request, user_id):
    return update_user_active(request, user_id, active=0)


@login_required(login_url='/musictherapy/login')
def unarchive_user(request, user_id):
    return update_user_active(request, user_id, active=1)


def update_user_active(request, user_id, active):
    red = None
    if request.POST:
        red = request.POST.get('redirect')
    elif request.GET:
        red = request.GET.get('redirect')

    user = get_object_or_None(models.UserInfo, pk=user_id)
    if user:
        user.active = active
        user.save()
        if red:
            if red == "patients":
                return redirect(reverse('musictherapy:list'))
            elif red == "program":
                return redirect(reverse('musictherapy:program_detail', kwargs={'program_id': int(user.program.id)}))
            elif red == "all_users":
                return redirect(reverse('musictherapy:all_users'))
            else:
                return HttpResponse(200)
    return HttpResponse(404)
