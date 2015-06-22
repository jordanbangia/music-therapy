# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0017_communicationassessment_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationgoals',
            name='feelings_were_articulated',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='communicationgoals',
            name='opinions_given',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='communicationgoals',
            name='verbal_part_with_verbal_prompt',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='communicationgoals',
            name='verbal_part_without_verbal_prompt',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
