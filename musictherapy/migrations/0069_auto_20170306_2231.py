# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0068_auto_20170306_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.IntegerField(default=1, choices=[(0, b'Missed'), (1, b'Attended')]),
        ),
    ]
