from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
]
