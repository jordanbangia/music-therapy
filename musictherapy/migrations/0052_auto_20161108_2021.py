# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0051_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergoalmeasurables',
            name='session',
            field=models.ForeignKey(to='musictherapy.Session', null=True),
        ),
        migrations.AddField(
            model_name='usergoalnotemeasurable',
            name='session',
            field=models.ForeignKey(to='musictherapy.Session', null=True),
        ),
        migrations.AddField(
            model_name='usergoals',
            name='session',
            field=models.ForeignKey(to='musictherapy.Session', null=True),
        ),
        migrations.AlterField(
            model_name='usergoalmeasurables',
            name='user',
            field=models.ForeignKey(related_name='goalmeasurables', to='musictherapy.UserInfo', null=True),
        ),
        migrations.AlterField(
            model_name='usergoalnotemeasurable',
            name='user',
            field=models.ForeignKey(related_name='goalmeasurables_note', to='musictherapy.UserInfo', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('user', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoalmeasurables',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoalnotemeasurable',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoals',
            unique_together=set([]),
        ),
    ]
