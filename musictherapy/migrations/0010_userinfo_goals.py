# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0009_communicationgoalsupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='goals',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=65, null=True, choices=[(1, b'Increase range of affect'), (2, b'Increase self-esteem'), (3, b'Increase leadership role'), (4, b'Decrease restlessness'), (5, b'Increase pain management'), (6, b'Decrease compulsive/destructive behaviour'), (25, b'Decrease depressive symptoms'), (7, b'Increase frustration tolerance'), (8, b'Increase anxiety control'), (9, b'Stimulate and maintain mobility'), (10, b'Stimulate and maintain fine motor skills'), (11, b'Stimulate and maintain gross motor skills'), (12, b'Stimulate and maintain coordination'), (13, b'Increase level of communication'), (14, b'Increase self-expression'), (15, b'Increase choice making'), (16, b'Increase sensory stimulation'), (17, b'Maintain cognitive function'), (18, b'Decrease confusion and disorientation'), (19, b'Increase level of participation'), (20, b'Increase attention span'), (21, b'Decrease isolation'), (22, b'Increase social interaction'), (23, b'Maintain current knowledge of music'), (24, b'Maintain current music skills')]),
        ),
    ]
