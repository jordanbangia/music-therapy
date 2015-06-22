# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0015_auto_20150622_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationassessment',
            name='choice_making',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='interactive_speech',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='receptive_language',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='singing_vocal_skills',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='verbal_skills',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='vocalization',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
    ]
