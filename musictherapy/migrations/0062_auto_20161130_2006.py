# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0061_auto_20161124_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='program',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='program',
            field=models.ManyToManyField(to='musictherapy.Program', null=True, blank=True),
        ),
    ]
