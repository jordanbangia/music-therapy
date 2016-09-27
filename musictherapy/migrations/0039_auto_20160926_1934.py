# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0038_auto_20160925_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermeasurables',
            old_name='goal',
            new_name='measurable',
        ),
        migrations.AlterUniqueTogether(
            name='usermeasurables',
            unique_together=set([('user', 'measurable')]),
        ),
    ]
