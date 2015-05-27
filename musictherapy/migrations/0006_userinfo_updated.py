# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0005_auto_20150526_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 15, 2, 4, 966000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
