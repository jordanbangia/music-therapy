import django.contrib.auth.views as auth
from django.conf.urls import url

from musictherapy import views, export

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musictherapy/$', views.index, name='index'),
    url(r'^musictherapy/users/$', views.users, name='list'),
    url(r'^musictherapy/users/new/$', views.create_user, name='create_user'),
    url(r'^musictherapy/users/submit_userinfo/$', views.save_new_basic, name='new_userinfo'),
    url(r'^musictherapy/users/all/$', views.all_users, name='all_users'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/sessions/(?P<session_id>[0-9]+)/$', views.user_session_detail, name='user_session_detail'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_userinfo/$', views.save_basic_info, name='save_userinfo'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_musicpref/$', views.save_music_pref, name='save_musicpref'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/delete_user/$', views.delete_user, name='delete_user'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_measurables/$', views.save_measurables, name="save_measurables"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/sessions/(?P<session_id>[0-9]+)/submit_goalmeasurables/$', views.save_goalmeasurables, name="save_goalmeasurables"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_goalmeasurables/$', views.save_goalmeasurables_no_session, name="save_goalmeasurables_no_session"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/submit_goals/$', views.save_user_goals, name="save_goals"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/archive/$', views.archive_user, name="archive_user"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/unarchive/$', views.unarchive_user, name="unarchive_user"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/export/assessment/$', export.assessment, name="export_assessment"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/export/sessions/(?P<session_id>[0-9]+)/treatment_plan/$', export.treatment_plan, name="export_treatment"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/export/from/(?P<from_year>[0-9]+)/(?P<from_month>[0-9]+)/to/(?P<to_year>[0-9]+)/(?P<to_month>[0-9]+)/$', export.report, name="export_report"),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/sessions/(?P<session_id>[0-9]+)/save_session_status/$', views.save_session_info, name='save_session_status'),
    url(r'^musictherapy/users/(?P<user_id>[0-9]+)/create_session/$', views.create_session, name="create_session"),

    url(r'^musictherapy/staff/$', views.create_staff, name='create_staff'),
    url(r'^musictherapy/login/$', auth.login, {
        'template_name': 'musictherapy/login.html'
    }, name='login'),
    url(r'^musictherapy/logout/$', auth.logout, {
        'next_page': '/musictherapy'
    }, name='logout'),
    url(r'^musictherapy/change_password/$', auth.password_change, {
            'template_name': 'musictherapy/change_password.html',
            'post_change_redirect': '/musictherapy/clients?status=pass_change_success',
    }, name="password_change"),
    url(r'^musictherapy/programs/save_program', views.save_program, name='save_program'),
    url(r'^musictherapy/programs/(?P<program_id>[0-9]+)/$', views.program_detail, name='program_detail'),
]

