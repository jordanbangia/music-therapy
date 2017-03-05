# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0066_auto_20170228_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Attended'), (1, b'Missed')]),
        ),
    ]
