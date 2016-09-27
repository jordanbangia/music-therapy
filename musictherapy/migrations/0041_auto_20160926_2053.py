# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0040_auto_20160926_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermeasurables',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
