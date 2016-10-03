# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0044_auto_20161001_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDomainNoteMeasurables',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('domain', models.ForeignKey(related_name='domainmeasurablesnote', to='musictherapy.Domains')),
                ('user', models.ForeignKey(related_name='measurables_note', to='musictherapy.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserGoalNoteMeasurable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(default=b'', null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('domain', models.ForeignKey(to='musictherapy.Domains')),
                ('user', models.ForeignKey(related_name='goalmeasurables_note', to='musictherapy.UserInfo')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usergoalnotemeasurable',
            unique_together=set([('user', 'domain', 'updated')]),
        ),
        migrations.AlterUniqueTogether(
            name='userdomainnotemeasurables',
            unique_together=set([('user', 'domain', 'updated')]),
        ),
    ]
