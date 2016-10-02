# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0043_userinfo_program'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usergoalmeasurables',
            unique_together=set([('user', 'goal_measurable', 'updated')]),
        ),
    ]
