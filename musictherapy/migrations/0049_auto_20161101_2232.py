# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0048_auto_20161016_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='date',
            field=models.CharField(max_length=1, verbose_name=b'Program Dates', choices=[(b'1', b'September - February'), (b'2', b'March - August')]),
        ),
    ]
