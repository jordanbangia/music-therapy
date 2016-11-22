# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0058_auto_20161115_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalsmeasurables',
            name='goal',
            field=models.ForeignKey(related_name='goalsmeasurables', blank=True, to='musictherapy.Goals', null=True),
        ),
    ]
