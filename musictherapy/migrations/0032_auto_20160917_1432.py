# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0031_musicalpreference_other_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_composer',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Favourite Composer/Performer(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_instrument',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Favourite Instrument(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='fav_song',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Favourite Song(s)', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='asp_level',
            field=models.IntegerField(verbose_name=b'Level of Care', choices=[(1, 1), (2, 2), (3, 3)]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='care_plan',
            field=models.TextField(default=b'', verbose_name=b'Care Plan'),
        ),
    ]
