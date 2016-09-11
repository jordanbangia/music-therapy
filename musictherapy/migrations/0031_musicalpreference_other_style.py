# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0030_auto_20160911_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicalpreference',
            name='other_style',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
