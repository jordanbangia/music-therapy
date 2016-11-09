# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0054_auto_20161108_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='program',
        ),
    ]
