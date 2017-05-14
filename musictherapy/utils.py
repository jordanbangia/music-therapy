from collections import defaultdict
from django.shortcuts import get_object_or_404
from django.utils import timezone

from musictherapy.models import Session, Goals, UserGoals


def all_sessions(user):
    return Session.objects.filter(user=user).order_by('-date')


def current_session(user):
    today = timezone.now().date()
    try:
        session = Session.objects.get(user=user, date=today)
    except Session.DoesNotExist:
        session = Session(user=user, date=today)
        session.save()
    return session


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


def is_date_in_range(date, start=None, end=None):
    """
    Checks that a given date is between the start and the end date.  Assumes all three are comparable objects (ideally datetime or date).
    :param date:  The date to check.
    :param start: The start date, can be None.
    :param end: The end date, can be None.
    :return: boolean stating whether date is between start and end.  If both start and end are None, it will return true by default. 
    """
    date_is_in_range = True
    if start:
        date_is_in_range = date_is_in_range and date >= start
    if end:
        date_is_in_range = date_is_in_range and date <= end
    return date_is_in_range
