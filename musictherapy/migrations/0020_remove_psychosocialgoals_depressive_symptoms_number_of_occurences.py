# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0019_auto_20150921_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychosocialgoals',
            name='depressive_symptoms_number_of_occurences',
        ),
    ]
