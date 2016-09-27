# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0033_auto_20160917_1908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domainmeasurables',
            options={'verbose_name': 'Domain Measurables'},
        ),
        migrations.AlterModelOptions(
            name='domains',
            options={'verbose_name': 'Domains'},
        ),
        migrations.AlterModelOptions(
            name='goals',
            options={'verbose_name': 'Goals'},
        ),
        migrations.AlterModelOptions(
            name='goalsmeasurables',
            options={'verbose_name': 'Goals Measurables'},
        ),
    ]
