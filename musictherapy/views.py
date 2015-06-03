from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

from .models import UserInfo, MusicalPreference, InitialCommunicationSkills, CommunicationGoalsUpdate
from .forms import UserInfoForm, MusicalPrefForm, InitialCommunicationAssessmentForm, CommunicationSkillsForm

from annoying.functions import get_object_or_None
# Create your views here.


# class IndexView(generic.ListView):
# 	template_name = 'musictherapy/index.html'
# 	context_object_name = 'user_info_list'

# 	def get_queryset(self):
# 		return UserInfo.objects.all()

# class DetailView(generic.DetailView):
# 	model = UserInfo
# 	template = 'musictherapy/detail.html'

def index(request):
    user_info_list = UserInfo.objects.all()
    context = {
        'user_info_list': user_info_list,
    }
    return render(request, 'musictherapy/index.html', context)


def user_detail(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    user_form = UserInfoForm(instance = user)
    user_last_updated = user.updated

    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    musicpref_form = MusicalPrefForm(instance = musicpref)
    musicpref_last_updated = musicpref.updated if musicpref else None

    initial_com_skills = get_object_or_None(InitialCommunicationSkills, pk=user_id)
    initial_com_form = InitialCommunicationAssessmentForm(instance=initial_com_skills)
    com_updates = CommunicationGoalsUpdate.objects.filter(user=user).order_by('updated')
    com_update_form = CommunicationSkillsForm()

    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'user_last_updated' : user_last_updated,

        'musical_pref_form': musicpref_form,
        'musicpref_last_updated' : musicpref_last_updated,

        'initial_com_form' : initial_com_form,
        'com_updates': com_updates,
        'com_skills_form' : com_update_form,
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

def save_initial_com_skills(request, user_id):
    initialcomskills = get_object_or_None(InitialCommunicationSkills, pk=user_id)
    if request.method == 'POST':
        initialcomskills_form = InitialCommunicationAssessmentForm(request.POST, instance=initialcomskills)
        if initialcomskills_form.is_valid():
            initialcomskills_form.save()
            return redirect('/musictherapy/' + user_id)


def save_com_skills_update(request, user_id):
    if request.method == 'POST':
        update_form = CommunicationSkillsForm(request.POST)
        if update_form.is_valid():
            update = update_form.save(commit=False)
            update.user = get_object_or_404(UserInfo, pk=user_id)
            update.save()
            # update_form.save()
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