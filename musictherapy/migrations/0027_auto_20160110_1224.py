# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0025_auto_20160109_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='cognitivememoryskillsassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
        migrations.AddField(
            model_name='motorskillsassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
        migrations.AddField(
            model_name='musicskillsassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
        migrations.AddField(
            model_name='psychosocialassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
        migrations.AddField(
            model_name='socialskillsassessment',
            name='notes',
            field=models.TextField(default=b'', verbose_name=b'Notes'),
        ),
    ]
