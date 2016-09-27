# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0035_auto_20160917_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='domains',
            name='parent',
            field=models.ForeignKey(related_name='subcategories', blank=True, to='musictherapy.Domains', null=True),
        ),
    ]
