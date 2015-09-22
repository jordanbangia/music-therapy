from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

from .models import UserInfo, MusicalPreference, CommunicationAssessment, CommunicationGoals, PsychoSocialAssessment, PsychoSocialGoals, \
    MotorSkillsAssessment, MotorSkillsGoals
from .forms import UserInfoForm, MusicalPrefForm, CommunicationAssessmentForm, CommunicationSkillsForm, GoalsForm, \
    PsychoSocialSkillsAssessmentForm, PsychoSocialSkillsForm, MotorSkillsAssessmentForm, MotorSkillsForm
from .goals import Goals

from annoying.functions import get_object_or_None

def index(request):
    user_info_list = UserInfo.objects.all()
    context = {
        'user_info_list': user_info_list,
    }
    return render(request, 'musictherapy/index.html', context)

def user_detail(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    user_form = UserInfoForm(instance = user)
    goals_form = GoalsForm(instance=user)
    user_last_updated = user.updated

    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    musicpref_form = MusicalPrefForm(instance = musicpref)
    musicpref_last_updated = musicpref.updated if musicpref else None

    com_assessments = CommunicationAssessment.objects.filter(user=user).order_by('updated')
    com_assessment_form = CommunicationAssessmentForm()
    com_updates = CommunicationGoals.objects.filter(user=user).order_by('updated')
    com_update_form = CommunicationSkillsForm(user=user)
    try:
        user_com_skills = CommunicationAssessment.objects.latest('updated')
    except:
        user_com_skills = None
    has_com_goals = Goals.has_communication_goals(user)

    pss_assessments = PsychoSocialAssessment.objects.filter(user=user).order_by('updated')
    pss_assessment_form = PsychoSocialSkillsAssessmentForm()
    pss_updates = PsychoSocialGoals.objects.filter(user=user).order_by('updated')
    pss_update_form = PsychoSocialSkillsForm(user=user)
    try:
        user_pss_skills = PsychoSocialAssessment.objects.latest('updated')
    except:
        user_pss_skills = None
    has_pss_goals = Goals.has_psycho_social_goals(user)

    motor_assessments = MotorSkillsAssessment.objects.filter(user=user).order_by('updated')
    motor_assessment_form = MotorSkillsAssessmentForm()
    motor_updates = MotorSkillsGoals.objects.filter(user=user).order_by('updated')
    motor_update_form = MotorSkillsForm(user=user)
    try:
        user_motor_skills = MotorSkillsAssessment.objects.latest('updated')
    except:
        user_motor_skills = None
    has_motor_goals = Goals.has_motor_goals(user)


    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'goals_form' : goals_form,
        'user_last_updated' : user_last_updated,

        'user_com_skills' : user_com_skills,
        'user_pss_skills' : user_pss_skills,
        'user_motor_skills' :  user_motor_skills,

        'musical_pref_form': musicpref_form,
        'musicpref_last_updated' : musicpref_last_updated,

        'com_assessment_form' : com_assessment_form,
        'com_assessments' : com_assessments,
        'com_updates': com_updates,
        'com_skills_form' : com_update_form,
        'has_com_goals' : has_com_goals,

        'pss_assessment_form' : pss_assessment_form,
        'pss_assessments' : pss_assessments,
        'pss_updates' : pss_updates,
        'pss_skills_form' : pss_update_form,
        'has_pss_goals' : has_pss_goals,

        'motor_assessment_form' : motor_assessment_form,
        'motor_assessments' : motor_assessments,
        'motor_updates' : motor_updates,
        'motor_skills_form' : motor_update_form,
        'has_motor_goals' : has_motor_goals,
    })

def save_basic_info(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/musictherapy/' + user_id)

def save_music_pref(request, user_id):
    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = MusicalPrefForm(request.POST, instance=musicpref)
        if musicpref_form.is_valid():
            musicpref_form.save()
            return redirect('/musictherapy/' + user_id)

def save_com_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(CommunicationAssessmentForm(request.POST), user_id)


def save_com_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(CommunicationSkillsForm(request.POST), user_id)


def save_pss_assess(request, user_id):
    if request.method == 'POST':
        return save_assess_form(PsychoSocialSkillsAssessmentForm(request.POST), user_id)


def save_pss_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(PsychoSocialSkillsForm(request.POST), user_id)


def save_motor_assess(request, user_id):
    print('hello')
    if request.method == 'POST':
        print('hi')
        return save_assess_form(MotorSkillsAssessmentForm(request.POST), user_id)


def save_motor_goals(request, user_id):
    if request.method == 'POST':
        return save_skills_form(MotorSkillsForm(request.POST), user_id)


def save_skills_form(form, user_id):
    if form.is_valid():
        update = form.save(commit=False)
        update.user = get_object_or_404(UserInfo, pk=user_id)
        update.save()
        return redirect('/musictherapy/' + user_id)


def save_assess_form(form, user_id):
    if form.is_valid():
        print('what up')
        update = form.save(commit=False)
        update.fill_measurables()
        update.user = get_object_or_404(UserInfo, pk=user_id)
        update.save()
        return redirect('/musictherapy/' + user_id)

def create_user(request):
    user_form = UserInfoForm()
    return render(request, 'musictherapy/detail.html', {
        'user_info_form' : user_form,
        'new' : True
    })


def save_new_basic(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('/musictherapy/' + str(user.pk), {
                'tab' : 'user_info',
            });
        else:
            print("From was not valid")
            return HttpResponse(404)


def delete_user(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    user.delete()
    return redirect('/musictherapy/')


def save_user_goals(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.method == 'POST':
        goals_form = GoalsForm(request.POST, instance=user)
        if goals_form.is_valid():
            goals_form.save()
            return redirect('/musictherapy/' + user_id)