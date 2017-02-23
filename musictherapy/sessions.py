from datetime import datetime

from django.shortcuts import get_object_or_404

from musictherapy.models import Session


def get_all_sessions(user):
    return Session.objects.filter(user=user).order_by('-date')


def get_current_session(user):
    sessions = get_all_sessions(user)
    if len(sessions) > 0 and sessions[0].date.date() == datetime.utcnow().date():
        current_session = sessions[0]
    else:
        current_session = Session(user=user)
        current_session.save()
    return current_session


def get_latest_session(user):
    sessions = get_all_sessions(user)
    if len(sessions) > 0:
        return sessions[0]
    return None


def get_session_for_id(user, session_id):
    # make sure that the latest session exists
    get_current_session(user)
    return get_object_or_404(Session, pk=session_id)
