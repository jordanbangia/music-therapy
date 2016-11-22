# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0059_auto_20161115_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='is_custom',
            field=models.IntegerField(default=0, choices=[(0, b'Not Custom'), (1, b'Custom')]),
        ),
        migrations.AddField(
            model_name='goals',
            name='user',
            field=models.ForeignKey(blank=True, to='musictherapy.UserInfo', null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='domain',
            field=models.ForeignKey(related_name='goals', to='musictherapy.Domains', null=True),
        ),
        migrations.AlterField(
            model_name='usergoals',
            name='user',
            field=models.ForeignKey(to='musictherapy.UserInfo', null=True),
        ),
    ]
