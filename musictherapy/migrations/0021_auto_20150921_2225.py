# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0020_remove_psychosocialgoals_depressive_symptoms_number_of_occurences'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psychosocialgoals',
            old_name='frustration_tolerance_number_of_occurences',
            new_name='frustration_tolerance_number_of_occurrences',
        ),
    ]
