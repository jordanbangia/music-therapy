# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('musictherapy', '0050_auto_20161108_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Session Date')),
                ('user', models.ForeignKey(related_name='sessions', to='musictherapy.UserInfo')),
            ],
        ),
    ]