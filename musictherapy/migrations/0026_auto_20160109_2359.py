# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import musictherapy.models


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0025_auto_20160109_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='goals',
            field=musictherapy.models.GoalsSelectField(max_length=200, null=True, blank=True),
        ),
    ]
