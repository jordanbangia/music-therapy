from datetime import datetime

from collections import defaultdict
from django.shortcuts import get_object_or_404

from musictherapy.models import Session, Goals, UserGoals


def all_sessions(user):
    return Session.objects.filter(user=user).order_by('-date')


def current_session(user):
    sessions = all_sessions(user)
    if len(sessions) > 0 and sessions[0].date.date() == datetime.utcnow().date():
        session = sessions[0]
    else:
        session = Session(user=user)
        session.save()
    return session


def latest_session(user):
    sessions = all_sessions(user)
    if len(sessions) > 0:
        return sessions[0]
    return None


def session_for_id(user, session_id):
    # make sure that the latest session exists
    current_session(user)
    return get_object_or_404(Session, pk=session_id, user=user)


def users_goals(user):
    goals = defaultdict(list)
    for g in Goals.objects.filter(parent=None, enabled=1).order_by('domain'):
        if g.domain:
            if not g.is_custom or (g.is_custom and g.user == user):
                goals[g.domain.name if g.domain.parent is None else g.domain.parent.name] += [g]
    goals = dict(goals)
    goals['order'] = ['General'] + [domain for domain in goals.keys() if domain not in ('General', 'Custom')]
    if 'Custom' in goals:
        goals['order'] += ['Custom']
    goals['user'] = [ug.goal.pk for ug in UserGoals.objects.filter(user=user)]
    return goals
