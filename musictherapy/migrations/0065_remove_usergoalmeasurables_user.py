# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0064_auto_20170211_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergoalmeasurables',
            name='user',
        ),
    ]
