# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0057_userinfo_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalsmeasurables',
            name='is_custom',
            field=models.IntegerField(default=0, choices=[(0, b'Not Custom'), (1, b'Custom')]),
        ),
        migrations.AddField(
            model_name='goalsmeasurables',
            name='user',
            field=models.ForeignKey(blank=True, to='musictherapy.UserInfo', null=True),
        ),
    ]
