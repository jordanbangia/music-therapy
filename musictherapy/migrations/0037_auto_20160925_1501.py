# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0036_domains_parent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usergoalmeasurables',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='usergoals',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='usermeasurables',
            unique_together=set([]),
        ),
    ]
