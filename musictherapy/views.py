from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from .models import UserInfo
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
	return render(request, 'musictherapy/detail.html', {'user_info' : user})