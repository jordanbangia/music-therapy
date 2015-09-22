from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
    url(r'^(?P<user_id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^(?P<user_id>[0-9]+)/submit_comassess/$',
        views.save_com_assess, name="save_commassessment"),
    url(r'^(?P<user_id>[0-9]+)/submit_comgoals/$',
        views.save_com_goals, name="save_comgoals"),
    url(r'^(?P<user_id>[0-9]+)/submit_pssassess/$',
        views.save_pss_assess, name="save_pssassessment"),
    url(r'^(?P<user_id>[0-9]+)/submit_pssgoals/$',
        views.save_pss_goals, name="save_pssgoals"),
    url(r'^(?P<user_id>[0-9]+)/submit_goals/$', views.save_user_goals, name="save_goals"),
    url(r'^new/$', views.create_user, name='create_user'),
    url(r'^new/submit_userinfo/$', views.save_new_basic, name='new_userinfo'),

]
