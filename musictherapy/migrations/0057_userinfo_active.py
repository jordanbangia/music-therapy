# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0056_userinfo_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='active',
            field=models.IntegerField(default=1, choices=[(0, b'archived'), (1, b'active')]),
        ),
    ]
