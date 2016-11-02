# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0047_auto_20161010_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='date',
            field=models.CharField(default=1, max_length=1, verbose_name=b'Program Dates', choices=[(1, b'September - February'), (2, b'March - August')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='day_of_week',
            field=models.CharField(default='mon', max_length=3, verbose_name=b'Day of Week', choices=[(b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednesday'), (b'thu', b'Thursday'), (b'fri', b'Friday'), (b'sat', b'Saturday'), (b'sun', b'Sunday')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(default=b'', null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('name', 'date', 'day_of_week', 'location', 'time')]),
        ),
        migrations.RemoveField(
            model_name='program',
            name='end',
        ),
        migrations.RemoveField(
            model_name='program',
            name='start',
        ),
    ]
