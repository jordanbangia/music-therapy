# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0002_auto_20150525_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='diagnosis',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
