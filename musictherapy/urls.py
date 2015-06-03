from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
    url(r'^(?P<user_id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^(?P<user_id>[0-9]+)/submit_initialcomskills/$', views.save_initial_com_skills, name="save_initialcomskills"),
    url(r'^(?P<user_id>[0-9]+)/submit_communicationskillsupdate/$', views.save_com_skills_update, name="save_commskillsupdate"),
    url(r'^new/$', views.create_user, name='create_user'),
    url(r'^new/submit_userinfo/$', views.save_new_basic, name='new_userinfo'),
]
