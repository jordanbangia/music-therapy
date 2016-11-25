# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0060_auto_20161116_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicalpreference',
            name='ethnic',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='musicalpreference',
            name='sacred_music',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='musicalpreference',
            name='preferred_style',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=252, null=True, choices=[(b'Big Band', b'Big Band'), (b'Broadway/Movie Musicals', b'Broadway/Movie Musicals'), (b'Classical Instrumental', b'Classical Instrumental'), (b'Classical Vocal', b'Classical Vocal'), (b'Easy Listening', b'Easy Listening'), (b'Folk', b'Folk'), (b'Bluegrass', b'Bluegrass'), (b'Gospel', b'Gospel'), (b'Opera', b'Opera'), (b'Country and Western', b'Country and Western'), (b"Rock 'n' Roll", b"Rock 'n' Roll"), (b'Motown', b'Motown'), (b'Jazz', b'Jazz'), (b'Marching Band', b'Marching Band'), (b'Meditative', b'Meditative'), (b'Musical TV Shows', b'Musical TV Shows'), (b'Ragtime', b'Ragtime'), (b'Pop Music', b'Pop Music'), (b'Rhythm and Blues', b'Rhythm and Blues'), (b'Soul', b'Soul'), (b'Patriotic', b'Patriotic')]),
        ),
    ]
