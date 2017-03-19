# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0069_auto_20170306_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='day_of_week',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name=b'Day of Week', choices=[(b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednesday'), (b'thu', b'Thursday'), (b'fri', b'Friday'), (b'sat', b'Saturday'), (b'sun', b'Sunday')]),
        ),
        migrations.AlterField(
            model_name='program',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Location', choices=[(b'Brampton', b'Brampton'), (b'Brunel', b'Brunel'), (b'Meadowvale', b'Meadowvale'), (b'Sam McCallion', b'Sam McCallion'), (b"Evelyn's", b"Evelyn's")]),
        ),
        migrations.AlterField(
            model_name='program',
            name='time',
            field=models.TimeField(null=True, verbose_name=b'Time', blank=True),
        ),
    ]
