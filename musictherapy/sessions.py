from datetime import datetime

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
