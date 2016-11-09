from django.conf.urls import url

from musictherapy import views
import django.contrib.auth.views as auth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musictherapy/$', views.index, name='index'),
    url(r'^musictherapy/users/$', views.patients, name='list'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^musictherapy/musicpref/(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^musictherapy/measurables/(?P<user_id>[0-9]+)/submit_measurables/$', views.save_measurables, name="save_measurables"),
    url(r'^musictherapy/goal_measurables/(?P<user_id>[0-9]+)/submit_goalmeasurables/$', views.save_goalmeasurables, name="save_goalmeasurables"),
    url(r'^musictherapy/goals/(?P<user_id>[0-9]+)/submit_goals/$', views.save_user_goals, name="save_goals"),
    url(r'^musictherapy/users/new/$', views.create_user, name='create_user'),
    url(r'^musictherapy/staff/$', views.create_staff, name='create_staff'),
    url(r'^musictherapy/users/submit_userinfo/$', views.save_new_basic, name='new_userinfo'),
    url(r'^musictherapy/login/$', auth.login, {
        'template_name': 'musictherapy/index.html'
    }, name='login'),
    url(r'^musictherapy/logout/$', auth.logout, {
        'next_page': '/musictherapy'
    }, name='logout'),
    url(r'^musictherapy/change_password/$', auth.password_change, {
            'template_name': 'musictherapy/change_password.html',
            'post_change_redirect': '/musictherapy/patients?status=pass_change_success',
    }, name="password_change"),
    url(r'^musictherapy/programs/save_program', views.save_program, name='save_program'),
    url(r'^musictherapy/programs/(?P<program_id>[0-9]+)/$', views.program_detail, name='program_detail'),
]

