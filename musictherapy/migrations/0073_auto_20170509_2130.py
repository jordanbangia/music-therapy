# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0072_session_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date2',
            field=models.DateField(verbose_name=b'Session Date 2'),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('user', 'date2')]),
        ),
        migrations.RemoveField(
            model_name='session',
            name='date',
        ),
    ]
