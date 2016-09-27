# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0032_auto_20160917_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainMeasurables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pos_neg', models.IntegerField(choices=[(1, b'Positive'), (-1, b'Negative')])),
                ('name', models.CharField(max_length=300)),
                ('enabled', models.IntegerField(choices=[(0, b'Disabled'), (1, b'Enabled')])),
            ],
        ),
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.IntegerField(choices=[(0, b'Disabled'), (1, b'Enabled')])),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('enabled', models.IntegerField(choices=[(0, b'Disabled'), (1, b'Enabled')])),
                ('domain', models.ForeignKey(related_name='goals', to='musictherapy.Domains')),
                ('parent', models.ForeignKey(related_name='subgoals', blank=True, to='musictherapy.Goals', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoalsMeasurables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('enabled', models.IntegerField(choices=[(0, b'Disabled'), (1, b'Enabled')])),
                ('goal', models.ForeignKey(related_name='goalsmeasurables', to='musictherapy.Goals')),
            ],
        ),
        migrations.CreateModel(
            name='UserGoalMeasurables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('goal_measurable', models.ForeignKey(to='musictherapy.GoalsMeasurables')),
            ],
        ),
        migrations.CreateModel(
            name='UserGoals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goal', models.ForeignKey(to='musictherapy.Goals')),
            ],
        ),
        migrations.CreateModel(
            name='UserMeasurables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('goal', models.ForeignKey(to='musictherapy.DomainMeasurables')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='goals',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='asp_level',
            field=models.IntegerField(verbose_name=b'Alzheimer Society Peel Level of Care', choices=[(1, 1), (2, 2), (3, 3)]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='care_plan',
            field=models.TextField(default=b'', verbose_name=b'Alzheimer Society Peel Care Plan'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='country_of_origin',
            field=models.CharField(max_length=100, verbose_name=b'Country of Origin'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='date_of_birth',
            field=models.DateField(verbose_name=b'Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='diagnosis',
            field=models.CharField(max_length=500, verbose_name=b'Diagnosis', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='history',
            field=models.CharField(max_length=500, verbose_name=b'Life Experiences/History'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='language_spoken',
            field=models.CharField(max_length=100, verbose_name=b'Language Spoken'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(max_length=100, verbose_name=b'Location', choices=[(b'Brampton', b'Brampton'), (b'Brunel', b'Brunel'), (b'Meadowvale', b'Meadowvale'), (b'Sam McCallion', b'Sam McCallion'), (b"Evelyn's", b"Evelyn's")]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='musical_history',
            field=models.CharField(max_length=500, verbose_name=b'Musical History'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'Name'),
        ),
        migrations.AddField(
            model_name='usermeasurables',
            name='user',
            field=models.ForeignKey(related_name='measurables', to='musictherapy.UserInfo'),
        ),
        migrations.AddField(
            model_name='usergoals',
            name='user',
            field=models.ForeignKey(related_name='goals', to='musictherapy.UserInfo'),
        ),
        migrations.AddField(
            model_name='usergoalmeasurables',
            name='user',
            field=models.ForeignKey(related_name='goalmeasurables', to='musictherapy.UserInfo'),
        ),
        migrations.AddField(
            model_name='domainmeasurables',
            name='domain',
            field=models.ForeignKey(related_name='domainmeasurables', to='musictherapy.Domains'),
        ),
        migrations.AlterUniqueTogether(
            name='usermeasurables',
            unique_together=set([('user', 'goal')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoals',
            unique_together=set([('user', 'goal')]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoalmeasurables',
            unique_together=set([('user', 'goal_measurable')]),
        ),
    ]
