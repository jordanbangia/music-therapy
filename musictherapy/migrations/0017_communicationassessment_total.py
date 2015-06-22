# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0016_auto_20150622_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationassessment',
            name='total',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
    ]
