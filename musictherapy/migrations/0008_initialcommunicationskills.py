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
                ('user', models.OneToOneField(primary_key=True, serialize=False, to='musictherapy.UserInfo')),
                ('verbalize_choices', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('fill_in_the_blank', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('engage_in_conv', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('answer_questions', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('song_writing', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('communicated_with_single_words', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('communicated_with_phrases', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('communicated_with_sentences', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('disjointed_response', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('appropriate_rate_of_speech', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('word_finding_difficulty', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('imitate_therapist', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('follow_directions', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('response_to_verbal_instr', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('respond_to_name_song', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('respond_to_hello_goodbye', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('call_and_response', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('singing_familiar_songs', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('sing_familiar_songs_syllables', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('greet_others', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
                ('make_choice_in_song', models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')])),
            ],
        ),
    ]
