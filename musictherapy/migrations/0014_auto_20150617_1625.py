# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0013_auto_20150617_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationassessment',
            name='answer_questions',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='appropriate_rate_of_speech',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='call_and_response',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_phrases',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_sentences',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_single_words',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='disjointed_response',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='engage_in_conv',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='follow_directions',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='greet_others',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='imitate_therapist',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='make_choice_in_song',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='respond_to_hello_goodbye',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='respond_to_name_song',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='response_to_verbal_instr',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='sing_familiar_songs_syllables',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='singing_familiar_songs',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='song_writing',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='word_finding_difficulty',
            field=models.IntegerField(choices=[(3, b'High/ Always'), (0, b'None/ Never'), (2, b'Medium/ Sometimes'), (1, b'Low/ Rarely')]),
        ),
    ]
