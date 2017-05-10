#!/usr/bin/env python
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")
django.setup()

from annoying.functions import get_object_or_None
import musictherapy.models as models


def fix_sessions():
    sessions = models.Session.objects.all()
    for s in sessions:
        s.date2 = s.date.date()
        s.save()

if __name__ == "__main__":
    fix_sessions()
