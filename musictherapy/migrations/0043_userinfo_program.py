# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0042_auto_20161001_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='program',
            field=models.TextField(default=b'', null=True, verbose_name=b'Program', blank=True),
        ),
    ]
