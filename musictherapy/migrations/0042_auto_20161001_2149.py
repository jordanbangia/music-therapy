# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0041_auto_20160926_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergoalmeasurables',
            name='updated',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=multiselectfield.db.fields.MultiSelectField(max_length=100, verbose_name=b'Location', choices=[(b'Brampton', b'Brampton'), (b'Brunel', b'Brunel'), (b'Meadowvale', b'Meadowvale'), (b'Sam McCallion', b'Sam McCallion'), (b"Evelyn's", b"Evelyn's")]),
        ),
    ]
