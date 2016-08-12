# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('musictherapy', '0028_default_groups_and_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='follow_non_verbal_directions',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='follow_verbal_directions',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='follows_hand_over_hand_directions',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='long_term_memory',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='maintains_synchrony_with_another',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='organize_thoughts',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='oriented_place',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='oriented_time',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='play_instruments',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='read_song_sheet_book',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='recalls_lyrics_familiar_songs',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='recalls_melody_familiar_songs',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='recalls_name_familiar_persons',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='recalls_own_name',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='recognize_error_self_correct',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='remains_on_task',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='short_term_memory',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='cognitivememoryskillsassessment',
            name='starts_stops_correct',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='answer_questions',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='appropriate_rate_of_speech',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='call_and_response',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='choice_making',
            field=models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_phrases',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_sentences',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='communicated_with_single_words',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='disjointed_response',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='engage_in_conv',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='fill_in_the_blank',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='follow_directions',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='greet_others',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='imitate_therapist',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='interactive_speech',
            field=models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='make_choice_in_song',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='receptive_language',
            field=models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='respond_to_hello_goodbye',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='respond_to_name_song',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='response_to_verbal_instr',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='sing_familiar_songs_syllables',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='singing_familiar_songs',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='singing_vocal_skills',
            field=models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='song_writing',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='verbalize_choices',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='vocalization',
            field=models.FloatField(default=-1, validators=[django.core.validators.MaxValueValidator(101)]),
        ),
        migrations.AlterField(
            model_name='communicationassessment',
            name='word_finding_difficulty',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='crosses_midline',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='demonstrated_adequate_body_coordination',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='demonstrated_finger_independence',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='demonstrated_upper_extremity_control',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='demonstrates_adequate_eye_hand_coordination',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='endurance',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='full_hearing',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='full_sight',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='gait',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='grasped_instruments_mallets',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='independent_mobility',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='range_of_motion',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='reach_for_instrument',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='structure_dance',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='motorskillsassessment',
            name='turn_pages_of_songbook',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='adapt_to_rhythmic_changes',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='choose_instrument_play',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='choose_song_style',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='discriminates_duration',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='discriminates_dynamics',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='familiar_song_title_lyrics',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='familiar_song_title_melody',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='finish_musical_phrase',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='keep_steady_beat',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='match_pitch',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='match_rhythm',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='response_to_music',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='musicskillsassessment',
            name='sing_familiar_songs',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='psychosocialassessment',
            name='display_range_of_affect',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='psychosocialassessment',
            name='self_esteem_confidence',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='psychosocialassessment',
            name='sense_of_humour',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='accept_leadership',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='active_in_session',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='attend_task',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='converse_others',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='dancing_others',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='engage_imitation',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='make_maintain_eye_contact',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='pass_exchange_instrument',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='passing_sharing_instruments',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='play_response_name',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
        migrations.AlterField(
            model_name='socialskillsassessment',
            name='remain_in_group',
            field=models.IntegerField(choices=[(-1, b'Not Measured'), (0, b'None/ Never'), (1, b'Low/ Rarely'), (2, b'Medium/ Sometimes'), (3, b'High/ Always')]),
        ),
    ]
