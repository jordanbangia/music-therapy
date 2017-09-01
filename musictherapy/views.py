import json
from collections import defaultdict
from datetime import datetime

import django.contrib.auth.views as auth
from annoying.functions import get_object_or_None
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods, require_GET

import musictherapy.forms as forms
import musictherapy.models as models
import musictherapy.utils as utils
from musictherapy.skills_data import SkillsData, SKILLS_PREFIX_DICT, prefix_to_domain

LOGIN_URL = '/musictherapy/login'

STATUS_MESSAGES = {
    'no_permission': 'You do not have permission to use this function.  Talk to an administrator if you have further questions.',
    'pass_change_success': 'Password changed successfully.',
    'staff_added': 'Staff member added successfully.'
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
@login_required(login_url=LOGIN_URL)
def users(request):
    status = request.GET.get('status', None)
    user_info_list = models.UserInfo.objects.all().filter(active=1).order_by('location')
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/clients.html', context)


@login_required(login_url=LOGIN_URL)
def all_users(request):
    status = request.GET.get('status', None)
    user_info_list = models.UserInfo.objects.all().order_by('location')
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/base/all_users.html', context)


@login_required(login_url=LOGIN_URL)
def user_detail(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    session = utils.current_session(user)

    return redirect(reverse('musictherapy:user_session_detail', kwargs={
        'user_id': int(user.pk),
        'session_id': int(session.pk)
    }))


@login_required(login_url=LOGIN_URL)
def user_session_detail(request, user_id, session_id):
    start = datetime.now()
    user = get_object_or_404(models.UserInfo, pk=user_id)
    session = utils.session_for_id(user, session_id)
    user_form = forms.UserInfoForm(instance=user)
    program_form = forms.ProgramForm()
    create_session_form = forms.SessionForm(instance=models.Session(user=user, date=timezone.now()))
    musicpref = get_object_or_None(models.MusicalPreference, pk=user_id)
    musicpref_form = forms.MusicalPrefForm(instance=musicpref, user_id=user_id)
    session_form = forms.SessionStatusForm(instance=session, user_id=user_id, session_id=session_id)
    all_sessions = utils.all_sessions(user)
    load_forms = datetime.now()
    all_goals = utils.users_goals(user)
    print("Took {} to load all forms and pre stuff for user detail".format(load_forms - start))

    d = {prefix: SkillsData(domain, user, session).to_dict() for domain, prefix in SKILLS_PREFIX_DICT.iteritems()}
    load_skills = datetime.now()
    print("Took {} to load skills data for user detail".format(load_skills - load_forms))

    return render(request, 'musictherapy/user_detail.html', {
        'userinfo': user,
        'user_info_form': user_form,
        'program_form': program_form,
        'sessions': all_sessions,
        'musical_pref_form': musicpref_form,
        'musical_pref': musicpref,
        'tab': request.GET.get('tab', 'info'),
        'session': session,
        'session_form': session_form,
        'goals': all_goals,
        'data': d,
        'export_years': [x for x in xrange(2015, datetime.today().year + 1)],
        'create_session_form': create_session_form,
    })


@login_required(login_url=LOGIN_URL)
def create_user(request):
    user_form = forms.UserInfoForm()
    program_form = forms.ProgramForm()
    return render(request, 'musictherapy/user_detail.html', {
        'user_info_form': user_form,
        'program_form': program_form,
        'tab': 'info',
        'new': True
    })


@login_required(login_url=LOGIN_URL)
def save_program(request):
    if request.method == 'POST':
        program_form = forms.ProgramForm(request.POST)
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


@login_required(login_url=LOGIN_URL)
def create_session(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(models.UserInfo, pk=user_id)
        session_form = forms.SessionForm(request.POST, instance=models.Session(user=user))
        if session_form.is_valid():
            session = session_form.save()
            return redirect(reverse('musictherapy:user_session_detail', kwargs={'user_id': int(user_id), 'session_id': int(session.pk)}))
        else:
            return HttpResponse(session_form.errors)
    return HttpResponse(404)


@login_required(login_url=LOGIN_URL)
def delete_session(request, user_id, session_id):
    if request.method == 'GET':
        session = get_object_or_404(models.Session, pk=session_id)
        session.delete()
        return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}))
    return redirect(reverse('musictherapy:user_session_detail', kwargs={'user_id': int(user_id), 'session_id': int(session_id)}))


@login_required(login_url=LOGIN_URL)
def save_new_basic(request):
    if request.method == 'POST':
        user_form = forms.UserInfoForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user.pk)}) + "?tab=info")
        return HttpResponse(user_form.errors)
    return HttpResponse(404)


@login_required(login_url=LOGIN_URL)
def save_basic_info(request, user_id):
    user = get_object_or_None(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = forms.UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab=info")
        return HttpResponse(user_form.errors)
    return HttpResponse(404)


@permission_required(perm='musictherapy.delete_userinfo')
@login_required(login_url=LOGIN_URL)
def delete_user(request, user_id):
    if request.user.has_perm('muscitherapy.userinfo.can_delete'):
        user = get_object_or_404(models.UserInfo, pk=user_id)
        user.delete()
        return redirect('/musictherapy/')
    else:
        return redirect('/musictherapy/users?status=no_permission')


@login_required(login_url=LOGIN_URL)
def save_user_goals(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    if request.method == 'POST':
        user_goals = [ug.pk for ug in models.UserGoals.objects.filter(user=user)]
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
            user_goal = models.UserGoals(goal=goal, user=user)
            user_goal.save()

        for goal in request.POST.getlist('goals', []):
            goal_model = models.Goals.objects.get(pk=goal)
            user_goal = get_object_or_None(models.UserGoals, goal=goal_model, user=user)
            if not user_goal:
                user_goal = models.UserGoals(user=user, goal=goal_model)
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
@login_required(login_url=LOGIN_URL)
def create_staff(request):
    if request.method == 'GET':
        context = {
            'staff_form': forms.StaffForm()
        }
        return render(request, 'musictherapy/staff.html', context)
    elif request.method == 'POST':
        staff_form = forms.StaffForm(request.POST)
        if staff_form.is_valid():
            staff_form.save()
            return redirect('/musictherapy/users?status=staff_added')
        else:
            return render(request, 'musictherapy/staff.html', {
                'staff_form': staff_form,
            })


@login_required(login_url=LOGIN_URL)
def save_music_pref(request, user_id):
    musicpref = get_object_or_None(models.MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = forms.MusicalPrefForm(request.POST, instance=musicpref, user_id=user_id)
        if musicpref_form.is_valid():
            if musicpref is None:
                musicpref = musicpref_form.save(commit=False)
                musicpref.user = get_object_or_404(models.UserInfo, pk=user_id)
            musicpref_form.save()
            return redirect(reverse('musictherapy:user_detail', kwargs={'user_id': int(user_id)}) + "?tab=musicpref")


@login_required(login_url=LOGIN_URL)
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
                domain = get_object_or_404(models.Domains, name=prefix_to_domain(domain_prefix))
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


@login_required(login_url=LOGIN_URL)
def save_goalmeasurables(request, user_id, session_id):
    if request.method == 'POST':
        data = request.POST.dict()
        user = get_object_or_404(models.UserInfo, pk=user_id)
        if session_id is not None:
            session = utils.session_for_id(user, session_id)
        else:
            session_date = datetime.strptime(data.pop('session_date'), '%Y/%m/%d')
            session_status = int(data.pop('session_status'))
            session_note = data.pop('session_note')

            session = utils.session_for_date(user, session_date)
            if session is None:
                session = models.Session(user=user, date=session_date, status=session_status, note=session_note)
                session.save()
                print("Created session for user: {}".format(user.id))
            else:
                print("Using session {} for user: {}".format(session.id, user.id))
        custom_gm = defaultdict(dict)

        try:
            for measurable_id, measurable_value in data.iteritems():
                if measurable_id.lower() in ['save', 'csrfmiddlewaretoken', 'submit', 'redirect', 'session']:
                    continue
                elif 'goalsnotes' in measurable_id.lower():
                    domain_prefix = measurable_id.lower().split('_')[0]
                    domain = get_object_or_404(models.Domains, name=prefix_to_domain(domain_prefix))
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
        except Exception as e:
            print(e)
    return HttpResponse(404)


@login_required(login_url=LOGIN_URL)
def save_goalmeasurables_no_session(request, user_id):
    return save_goalmeasurables(request, user_id, None)


@login_required(login_url=LOGIN_URL)
def program_detail(request, program_id):
    program = get_object_or_None(models.Program, pk=program_id)
    clients = models.UserInfo.objects.filter(program=program, active=1)
    return render(request, 'musictherapy/program_details.html', {
        'program': program,
        'users': clients,
        'date': timezone.now().date().isoformat().replace('-', '/')
    })


@login_required(login_url=LOGIN_URL)
def user_program_detail(request, user_id):
    user = get_object_or_404(models.UserInfo, pk=user_id)
    print
    data = {domain: SkillsData(domain, user, utils.current_session(user)).to_dict(program_data_only=True) for domain in SKILLS_PREFIX_DICT.keys()}
    return render(request, 'musictherapy/component/session_goals.html', {
        'data': data,
        'user': user,
        'session': None,
        'include_date': True,
        'date': timezone.now().date().isoformat().replace('-', '/')
    })


@login_required(login_url=LOGIN_URL)
def archive_user(request, user_id):
    return update_user_active(request, user_id, active=0)


@login_required(login_url=LOGIN_URL)
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
            if red == "clients":
                return redirect(reverse('musictherapy:list'))
            elif red == "program":
                return redirect(reverse('musictherapy:program_detail', kwargs={'program_id': int(user.program.id)}))
            elif red == "all_users":
                return redirect(reverse('musictherapy:all_users'))
            else:
                return HttpResponse(200)
    return HttpResponse(404)


@login_required(login_url=LOGIN_URL)
def save_session_info(request, user_id, session_id):
    if request.method == 'POST':
        user = get_object_or_404(models.UserInfo, pk=user_id)
        session = utils.session_for_id(user, session_id)
        session_form = forms.SessionStatusForm(request.POST, instance=session, user_id=user_id, session_id=session_id)

        if session_form.is_valid():
            session = session_form.save()
            session.save()
            return HttpResponse(200)
        else:
            print(session_form.errors)
    return HttpResponse(404)
