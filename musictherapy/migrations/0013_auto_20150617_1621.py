# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0012_auto_20150617_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationassessment',
            name='fill_in_the_blank',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
    ]
