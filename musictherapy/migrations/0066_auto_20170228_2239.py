# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0065_remove_usergoalmeasurables_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='history',
            field=models.TextField(verbose_name=b'Life Experiences/History'),
        ),
    ]
