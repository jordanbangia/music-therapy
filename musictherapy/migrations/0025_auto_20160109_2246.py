# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0024_auto_20160109_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='goals',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, null=True, blank=True),
        ),
    ]
