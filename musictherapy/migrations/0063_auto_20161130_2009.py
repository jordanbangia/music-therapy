# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0062_auto_20161130_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='program',
            field=models.ManyToManyField(to='musictherapy.Program', blank=True),
        ),
    ]
