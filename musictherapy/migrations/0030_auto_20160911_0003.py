# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0029_auto_20160811_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_composer',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_instrument',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_song',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
