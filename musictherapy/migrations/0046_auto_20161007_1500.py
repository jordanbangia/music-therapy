# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0045_auto_20161002_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='history',
            field=models.TextField(max_length=500, verbose_name=b'Life Experiences/History'),
        ),
    ]
