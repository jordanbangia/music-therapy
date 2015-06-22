# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0011_auto_20150617_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='communicationassessment',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 20, 13, 36, 814000, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='verbalize_choices',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
    ]
