from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
]