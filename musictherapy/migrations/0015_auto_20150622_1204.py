# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0014_auto_20150617_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationassessment',
            name='choice_making',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='interactive_speech',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='receptive_language',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='singing_vocal_skills',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='verbal_skills',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='communicationassessment',
            name='vocalization',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
