# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0034_auto_20160917_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domainmeasurables',
            options={'verbose_name': 'Domain Measurable'},
        ),
        migrations.AlterModelOptions(
            name='domains',
            options={'verbose_name': 'Domain'},
        ),
        migrations.AlterModelOptions(
            name='goals',
            options={'verbose_name': 'Goal'},
        ),
        migrations.AlterModelOptions(
            name='goalsmeasurables',
            options={'verbose_name': 'Goal Measurable'},
        ),
    ]
