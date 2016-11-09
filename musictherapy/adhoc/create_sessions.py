#!/usr/bin/env python
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")
django.setup()

from annoying.functions import get_object_or_None
import musictherapy.models as models


def fix_sessions():
    ug = models.UserGoals.objects.filter(session=None)
    for g in ug:
        if g.session is None:
            session = get_object_or_None(models.Session, user=g.user, date=g.updated)
            if not session:
                session = models.Session(user=g.user, date=g.updated)
                session.save()
            g.session = session
            g.save()

    ugm = models.UserGoalMeasurables.objects.filter(session=None)
    for g in ugm:
        if g.session is None:
            session = get_object_or_None(models.Session, user=g.user, date=g.updated)
            if not session:
                session = models.Session(user=g.user, date=g.updated)
                session.save()
            g.session = session
            g.save()

    ugnm = models.UserGoalNoteMeasurable.objects.filter(session=None)
    for g in ugnm:
        if g.session is None:
            session = get_object_or_None(models.Session, user=g.user, date=g.updated)
            if not session:
                session = models.Session(user=g.user, date=g.updated)
                session.save()
            g.session = session
            g.save()

if __name__ == "__main__":
    fix_sessions()
