# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0006_userinfo_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicalpreference',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 27, 16, 6, 27, 20000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
