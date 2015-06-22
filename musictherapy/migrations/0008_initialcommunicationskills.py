# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0007_musicalpreference_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialCommunicationSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='musictherapy.UserInfo')),
                ('verbalize_choices', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'),  (3, b'High/ Always')])),
                ('fill_in_the_blank', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('engage_in_conv', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('answer_questions', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('song_writing', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('communicated_with_single_words', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('communicated_with_phrases', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('communicated_with_sentences', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('disjointed_response', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('appropriate_rate_of_speech', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('word_finding_difficulty', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('imitate_therapist', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('follow_directions', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('response_to_verbal_instr', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('respond_to_name_song', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('respond_to_hello_goodbye', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('call_and_response', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('singing_familiar_songs', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('sing_familiar_songs_syllables', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('greet_others', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
                ('make_choice_in_song', models.IntegerField(choices=[(0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')])),
            ],
        ),
    ]
