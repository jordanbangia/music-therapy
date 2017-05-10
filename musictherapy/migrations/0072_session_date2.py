# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0071_auto_20170506_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date2',
            field=models.DateField(null=True, verbose_name=b'Session Date 2'),
        ),
    ]
