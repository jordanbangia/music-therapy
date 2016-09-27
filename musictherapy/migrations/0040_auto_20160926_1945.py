# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0039_auto_20160926_1934'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usermeasurables',
            unique_together=set([('user', 'measurable', 'updated')]),
        ),
    ]
