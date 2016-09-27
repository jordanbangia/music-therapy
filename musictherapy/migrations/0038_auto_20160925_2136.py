# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0037_auto_20160925_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergoalmeasurables',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usergoals',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='usermeasurables',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='usergoalmeasurables',
            unique_together=set([('user', 'goal_measurable')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoals',
            unique_together=set([('user', 'goal')]),
        ),
        migrations.AlterUniqueTogether(
            name='usermeasurables',
            unique_together=set([('user', 'goal')]),
        ),
    ]
