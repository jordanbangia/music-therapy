# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0021_auto_20150921_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='cognitionmemoryskillsgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='communicationgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='motorskillsgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='musicskillsgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='psychosocialgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='socialskillsgoals',
            name='notes',
            field=models.TextField(default=b''),
        ),
    ]
