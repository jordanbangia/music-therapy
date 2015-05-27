from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone

from .models import UserInfo, MusicalPreference
from .forms import UserInfoForm, MusicalPrefForm

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
    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    user_form = UserInfoForm(instance = user)
    user_last_updated = user.updated
    musicpref_form = MusicalPrefForm(instance = musicpref)
    musicpref_last_updated = musicpref.updated if musicpref else None

    return render(request, 'musictherapy/detail.html', {
        'user_info_form': user_form,
        'musical_pref_form': musicpref_form,
        'user_last_updated' : user_last_updated,
        'musicpref_last_updated' : musicpref_last_updated})

def save_basic_info(request, user_id):
    user = get_object_or_404(UserInfo, pk=user_id)
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/musictherapy/' + user_id, {
                'tab' : 'user_info',
            })

def save_music_pref(request, user_id):
    musicpref = get_object_or_None(MusicalPreference, pk=user_id)
    if request.method == 'POST':
        musicpref_form = MusicalPrefForm(request.POST, instance=musicpref)
        if musicpref_form.is_valid():
            musicpref_form.save()
            return redirect('/musictherapy/' + user_id,{
                'tab' : 'music_pref',
            })