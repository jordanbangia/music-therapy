# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0055_remove_userinfo_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='program',
            field=models.ForeignKey(blank=True, to='musictherapy.Program', null=True),
        ),
    ]
