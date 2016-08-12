from collections import namedtuple

import django.contrib.auth.views as auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_GET

import pygal
from annoying.functions import get_object_or_None

from musictherapy.forms import *
from musictherapy.models import *


SkillsData = namedtuple('SkillsData', ['chart', 'fields', 'assessments', 'assess_form', 'update_form', 'has_goals', 'goals_data'])
SummaryData = namedtuple('SummaryData', ['com', 'pss', 'motor', 'cog', 'social', 'music'])

STATUS_MESSAGES = {
    'no_permission': 'You do not have permission to use this function.  Talk to an administrator if you have further questions.',
    'pass_change_success': 'Password changed successfully.',
    'staff_added': 'Staff member added successfully.'
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
    user_info_list = UserInfo.objects.all()
    context = {
        'user_info_list': user_info_list,
        'status': STATUS_MESSAGES.get(status, None)
    }

    return render(request, 'musictherapy/patients.html', context)


@login_required(login_url='/musictherapy/login')
def user_detail(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    user_form = UserInfoForm(instance=user)
    goals_form = GoalsForm(instance=user)
    user_last_updated = user.updated

    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    musicpref_form = MusicalPrefForm(instance = musicpref)
    musicpref_last_updated = musicpref.updated if musicpref else None

    com_skills_data = SkillsData(assessments=CommunicationAssessment.objects.filter(user=user).order_by('updated'),
                                 assess_form=CommunicationAssessmentForm(),
                                 update_form=CommunicationSkillsForm(user=user),
                                 goals_data=CommunicationGoals.objects.filter(user=user).order_by('updated'),
                                 chart=make_chart(CommunicationGoals.objects.filter(user=user).order_by('updated'), Goals.has_communication_goals(user)),
                                 has_goals=Goals.has_communication_goals(user),
                                 fields=CommunicationAssessment.assessment_fields)

    pss_skills_data = SkillsData(assessments=PsychoSocialAssessment.objects.filter(user=user).order_by('updated'),
                                 assess_form=PsychoSocialSkillsAssessmentForm(),
                                 update_form=PsychoSocialSkillsForm(user=user),
                                 goals_data=PsychoSocialGoals.objects.filter(user=user).order_by('updated'),
                                 chart=make_chart(PsychoSocialGoals.objects.filter(user=user).order_by('updated'), Goals.has_psycho_social_goals(user)),
                                 has_goals=Goals.has_psycho_social_goals(user),
                                 fields=PsychoSocialAssessment.assessment_fields)

    motor_skills_data = SkillsData(assessments=MotorSkillsAssessment.objects.filter(user=user).order_by('updated'),
                                   assess_form=MotorSkillsAssessmentForm(),
                                   update_form=MotorSkillsForm(user=user),
                                   goals_data=MotorSkillsGoals.objects.filter(user=user).order_by('updated'),
                                   chart=make_chart(MotorSkillsGoals.objects.filter(user=user).order_by('updated'), Goals.has_motor_goals(user)),
                                   has_goals=Goals.has_motor_goals(user),
                                   fields=MotorSkillsAssessment.assessment_fields)

    cog_skills_data = SkillsData(assessments=CognitiveMemorySkillsAssessment.objects.filter(user=user).order_by('updated'),
                                 assess_form=CognitiveSkillsAssessmentForm(),
                                 update_form=CognitiveSkillsForm(user=user),
                                 goals_data=CognitionMemorySkillsGoals.objects.filter(user=user).order_by('updated'),
                                 chart=make_chart(CognitionMemorySkillsGoals.objects.filter(user=user).order_by('updated'), Goals.has_motor_goals(user)),
                                 has_goals=Goals.has_motor_goals(user),
                                 fields=CognitiveMemorySkillsAssessment.assessment_fields)

    social_skills_data = SkillsData(assessments=SocialSkillsAssessment.objects.filter(user=user).order_by('updated'),
                                    assess_form=SocialSkillsAssessmentForm(),
                                    update_form=SocialSkillsForm(user=user),
                                    goals_data=SocialSkillsGoals.objects.filter(user=user).order_by('updated'),
                                    chart=make_chart(SocialSkillsGoals.objects.filter(user=user).order_by('updated'), Goals.has_social_goals(user)),
                                    has_goals=Goals.has_social_goals(user),
                                    fields=SocialSkillsAssessment.assessment_fields)

    music_skills_data = SkillsData(assessments=MusicSkillsAssessment.objects.filter(user=user).order_by('updated'),
                                   assess_form=MusicSkillsAssessmentForm(),
                                   update_form=MusicSkillsForm(user=user),
                                   goals_data=MusicSkillsGoals.objects.filter(user=user).order_by('updated'),
                                   chart=make_chart(MusicSkillsGoals.objects.filter(user=user).order_by('updated'), Goals.has_music_goals(user)),
                                   has_goals=Goals.has_music_goals(user),
                                   fields=MusicSkillsAssessment.assessment_fields)

    summary = SummaryData(com=get_assessments(CommunicationAssessment, user),
                          pss=get_assessments(PsychoSocialAssessment, user),
                          motor=get_assessments(MotorSkillsAssessment, user),
                          social=get_assessments(SocialSkillsAssessment, user),
                          music=get_assessments(MusicSkillsAssessment, user),
                          cog=get_assessments(CognitiveMemorySkillsAssessment, user))

    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'goals_form': goals_form,
        'user_last_updated': user_last_updated,

        'summary': summary,

        'musical_pref_form': musicpref_form,
        'musicpref_last_updated': musicpref_last_updated,

        'com_data': com_skills_data,
        'pss_data': pss_skills_data,
        'motor_data': motor_skills_data,
        'cog_data': cog_skills_data,
        'social_data': social_skills_data,
        'music_data': music_skills_data,
    })


@login_required(login_url='/musictherapy/login')
def save_basic_info(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def save_music_pref(request, user_id):
    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = MusicalPrefForm(request.POST, instance=musicpref)
        if musicpref_form.is_valid():
            if musicpref:
                musicpref_form.save()
            else:
                musicpref = musicpref_form.save(commit=False)
                musicpref.user = get_object_or_404(UserInfo, pk=user_id)
            return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def save_com_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(CommunicationAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_com_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(CommunicationSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_pss_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(PsychoSocialSkillsAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_pss_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(PsychoSocialSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_motor_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(MotorSkillsAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_motor_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(MotorSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_cog_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(CognitiveSkillsAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_cog_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(CognitiveSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_social_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(SocialSkillsAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_social_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(SocialSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_music_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(MusicSkillsForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_music_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(MusicSkillsAssessmentForm(request.POST), user_id)


@login_required(login_url='/musictherapy/login')
def save_skills_form(form, user_id):
    if form.is_valid():
        update = form.save(commit=False)
        update.user = get_object_or_404(UserInfo, pk=user_id)
        update.save()
        return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def save_assess_form(form, user_id):
    if form.is_valid():
        update = form.save(commit=False)
        update.fill_measurables()
        update.user = get_object_or_404(UserInfo, pk=user_id)
        update.save()
        return redirect('/musictherapy/' + user_id)


@login_required(login_url='/musictherapy/login')
def create_user(request):
    user_form = UserInfoForm()
    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'new': True
    })


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
        user = get_object_or_404(UserInfo, pk=user_id)
        user.delete()
        return redirect('/musictherapy/')
    else:
        return redirect('/musictherapy/patients?status=no_permission')


@login_required(login_url='/musictherapy/login')
def save_user_goals(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.method == 'POST':
        goals_form = GoalsForm(request.POST, instance=user)
        if goals_form.is_valid():
            goals_form.save()
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


def make_chart(goals, has_goals):
    line_chart = pygal.Line()
    if has_goals:
        field_names = [field.attname for field in goals.model._meta.get_fields() if field.attname not in ["id", "user_id", "notes"]]
        lines = {field_name: list() for field_name in field_names}
        for goal in goals:
            for field in field_names:
                lines[field].append(getattr(goal, field))

        line_chart.x_labels = map(str, lines.pop('updated'))
        for field, values in lines.items():
            line_chart.add(field, values)
        return line_chart.render(is_unicode=True, disable_xml_declaration=True)
    else:
        return None


def get_assessments(assessment, user):
    try:
        return assessment.objects.filter(user=user).order_by('-updated')
    except:
        return None
