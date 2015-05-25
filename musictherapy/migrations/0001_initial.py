# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fav_composer', models.CharField(max_length=200)),
                ('fav_song', models.CharField(max_length=200)),
                ('fav_instrument', models.CharField(max_length=200)),
                ('preferred_style', multiselectfield.db.fields.MultiSelectField(blank=True, max_length=253, null=True, choices=[(b'Big Band', b'Big Band'), (b'Broadway/Movie Musicals', b'Broadway/Movie Musicals'), (b'Classical Instrumental', b'Classical Instrumental'), (b'Classical Vocal', b'Classical Vocal'), (b'Easy Listening', b'Easy Listening'), (b'Folk', b'Folk'), (b'Bluegrass', b'Bluegrass'), (b'Gospel', b'Gospel'), (b'Opera', b'Opera'), (b'Country and Western', b'Country and Western'), (b'Heavy Rock', b'Heavy Rock'), (b'Electronic', b'Electronic'), (b'Jazz', b'Jazz'), (b'Marching Band', b'Marching Band'), (b'Meditative', b'Meditative'), (b'Musical TV Shows', b'Musical TV Shows'), (b'Ragtime', b'Ragtime'), (b'Pop Music', b'Pop Music'), (b'Rhythm and Blues', b'Rhythm and Blues'), (b'Soul', b'Soul'), (b'Patriotic', b'Patriotic')])),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100, choices=[(b'Brampton', b'Brampton'), (b'Brunel', b'Brunel'), (b'Meadowvale', b'Meadowvale'), (b'Sam McCallion', b'Sam McCallion'), (b"Evelyn's", b"Evelyn's")])),
                ('date_of_birth', models.DateTimeField(verbose_name=b'DOB')),
                ('history', models.CharField(max_length=300)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('language_spoken', models.CharField(max_length=100)),
                ('musical_history', models.CharField(max_length=500)),
                ('care_plan', models.CharField(max_length=200)),
                ('asp_level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='musicalpreference',
            name='user',
            field=models.ForeignKey(to='musictherapy.UserInfo'),
        ),
    ]
