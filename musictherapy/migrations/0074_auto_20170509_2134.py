# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0073_auto_20170509_2130'),
    ]

    operations = [
        migrations.RenameField('Session', 'date2', 'date')
    ]
