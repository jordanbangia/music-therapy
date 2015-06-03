# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0008_initialcommunicationskills'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunicationGoalsUpdate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('verbal_part_with_verbal_prompt', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('verbal_part_without_verbal_prompt', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('feelings_were_articulated', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('opinions_given', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('user', models.ForeignKey(to='musictherapy.UserInfo')),
            ],
        ),
    ]
