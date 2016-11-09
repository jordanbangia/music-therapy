# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0046_auto_20161007_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Name')),
                ('start', models.DateField(verbose_name=b'Start Date')),
                ('end', models.DateField(verbose_name=b'End Date')),
                ('location', models.CharField(max_length=100, verbose_name=b'Location', choices=[(b'Brampton', b'Brampton'), (b'Brunel', b'Brunel'), (b'Meadowvale', b'Meadowvale'), (b'Sam McCallion', b'Sam McCallion'), (b"Evelyn's", b"Evelyn's")])),
                ('time', models.TimeField(verbose_name=b'Time')),
                ('description', models.TextField(default=b'', verbose_name=b'Description')),
            ],
        ),
        migrations.RemoveField(
            model_name='cognitionmemoryskillsgoals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cognitivememoryskillsassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='communicationassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='communicationgoals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='motorskillsassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='motorskillsgoals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='musicskillsassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='musicskillsgoals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='observablebehaviours',
            name='user',
        ),
        migrations.RemoveField(
            model_name='psychosocialassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='psychosocialgoals',
            name='user',
        ),
        migrations.RemoveField(
            model_name='socialskillsassessment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='socialskillsgoals',
            name='user',
        ),
        migrations.DeleteModel(
            name='CognitionMemorySkillsGoals',
        ),
        migrations.DeleteModel(
            name='CognitiveMemorySkillsAssessment',
        ),
        migrations.DeleteModel(
            name='CommunicationAssessment',
        ),
        migrations.DeleteModel(
            name='CommunicationGoals',
        ),
        migrations.DeleteModel(
            name='MotorSkillsAssessment',
        ),
        migrations.DeleteModel(
            name='MotorSkillsGoals',
        ),
        migrations.DeleteModel(
            name='MusicSkillsAssessment',
        ),
        migrations.DeleteModel(
            name='MusicSkillsGoals',
        ),
        migrations.DeleteModel(
            name='ObservableBehaviours',
        ),
        migrations.DeleteModel(
            name='PsychoSocialAssessment',
        ),
        migrations.DeleteModel(
            name='PsychoSocialGoals',
        ),
        migrations.DeleteModel(
            name='SocialSkillsAssessment',
        ),
        migrations.DeleteModel(
            name='SocialSkillsGoals',
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('name', 'start', 'end', 'location', 'time')]),
        ),
    ]
