# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0052_auto_20161108_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='program',
            field=models.ForeignKey(blank=True, to='musictherapy.Program', null=True),
        ),
    ]
