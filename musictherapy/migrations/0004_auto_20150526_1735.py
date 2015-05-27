# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0003_userinfo_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalpreference',
            name='user',
            field=models.OneToOneField(to='musictherapy.UserInfo'),
        ),
    ]
