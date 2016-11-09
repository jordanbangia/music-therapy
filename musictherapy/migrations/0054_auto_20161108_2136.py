# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0053_auto_20161108_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergoalmeasurables',
            name='goal_measurable',
            field=models.ForeignKey(to='musictherapy.GoalsMeasurables', null=True),
        ),
        migrations.AlterField(
            model_name='usergoals',
            name='user',
            field=models.ForeignKey(related_name='goals', to='musictherapy.UserInfo', null=True),
        ),
    ]
