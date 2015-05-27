# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0004_auto_20150526_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicalpreference',
            name='id',
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='user',
            field=models.OneToOneField(primary_key=True, serialize=False, to='musictherapy.UserInfo'),
        ),
    ]
