# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0067_auto_20170304_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Session Date'),
        ),
        migrations.AlterField(
            model_name='session',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
    ]
