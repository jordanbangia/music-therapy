from .models import UserInfo, MusicalPreference, CommunicationAssessment, CommunicationGoals, \
    PsychoSocialAssessment, PsychoSocialGoals, MotorSkillsAssessment, MotorSkillsGoals, \
    CognitiveMemorySkillsAssessment, CognitionMemorySkillsGoals
from .extras import SelectDateWidget
from .goals import Goals
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Accordion, AccordionGroup

class GoalsForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('goals',)

    def __init__(self, *args, **kwargs):
        super(GoalsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-goals'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_goals/#goals'
        self.helper.add_input(Submit('submit', 'Save'))


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('name', 'location', 'date_of_birth', 'diagnosis', 'history', 'country_of_origin', 'language_spoken',
                  'musical_history', 'care_plan', 'asp_level')
        widgets = {
            'date_of_birth' : SelectDateWidget
        }

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-userinfoform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_userinfo/#basicinfo'
        self.helper.add_input(Submit('submit', 'Save'))


class MusicalPrefForm(ModelForm):
    class Meta:
        model = MusicalPreference
        fields = ('fav_composer', 'fav_song', 'fav_instrument', 'preferred_style')

    def __init__(self, *args, **kwargs):
        super(MusicalPrefForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-musicalprefform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_musicpref/#musicpref'
        self.helper.add_input(Submit('submit', 'Save'))


class CommunicationAssessmentForm(ModelForm):
    class Meta:
        model = CommunicationAssessment
        fields = ('verbalize_choices', 'fill_in_the_blank', 'engage_in_conv', 'answer_questions', 'song_writing',
                  'communicated_with_single_words', 'communicated_with_phrases', 'communicated_with_sentences',
                  'disjointed_response', 'appropriate_rate_of_speech', 'word_finding_difficulty', 'imitate_therapist',
                  'follow_directions', 'response_to_verbal_instr', 'respond_to_name_song', 'respond_to_hello_goodbye',
                  'call_and_response', 'singing_familiar_songs', 'sing_familiar_songs_syllables', 'greet_others',
                  'make_choice_in_song')

    def __init__(self, *args, **kwargs):
        super(CommunicationAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-communicationassessment'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_comassess/#communicationskills'
        self.helper.add_input(Submit('submit', 'Submit Skills Assessment'))
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Communication Skills Assessment',
                               'verbalize_choices', 'fill_in_the_blank', 'engage_in_conv', 'answer_questions',
                               'song_writing', 'communicated_with_single_words', 'communicated_with_phrases',
                               'communicated_with_sentences', 'disjointed_response', 'appropriate_rate_of_speech',
                               'word_finding_difficulty', 'imitate_therapist', 'follow_directions',
                               'response_to_verbal_instr', 'respond_to_name_song', 'respond_to_hello_goodbye',
                               'call_and_response', 'singing_familiar_songs', 'sing_familiar_songs_syllables',
                               'greet_others', 'make_choice_in_song')
            )
        )


class CommunicationSkillsForm(ModelForm):
    class Meta:
        model = CommunicationGoals
        fields = ('verbal_part_with_verbal_prompt', 'verbal_part_without_verbal_prompt', 'feelings_were_articulated',
                  'opinions_given')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommunicationSkillsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-communicationgoals'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_comgoals/#communicationskills'
        self.helper.add_input(Submit('submit', 'Submit'))

        if user:
            user_goals = Goals.get_communication_goals(user)
            if Goals.COM_INCREASE_LEVEL not in user_goals:
                del self.fields['verbal_part_with_verbal_prompt']
                del self.fields['verbal_part_without_verbal_prompt']
            if Goals.COM_INCREASE_SELF_EXPRESSION not in  user_goals:
                del self.fields['feelings_were_articulated']
                del self.fields['opinions_given']


class PsychoSocialSkillsAssessmentForm(ModelForm):
    class Meta:
        model = PsychoSocialAssessment
        fields = ('display_range_of_affect', 'self_esteem_confidence', 'sense_of_humour')

    def __init__(self, *args, **kwargs):
        super(PsychoSocialSkillsAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-psychosocialassessment'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_pssassess/#psychosocialskills'
        self.helper.add_input(Submit('submit', 'Submit Skills Assessment'))
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Psycho-Social Skills Assessment',
                               'display_range_of_affect', 'self_esteem_confidence', 'sense_of_humour')
            )
        )


class PsychoSocialSkillsForm(ModelForm):
    class Meta:
        model = PsychoSocialGoals
        fields = ('smiled', 'frowned', 'made_negative_comments_self', 'made_positive_comments_self', 'refused_to_lead_activity',
                  'lead_activity', 'left_program', 'complained_of_pain', 'destructive_behaviour_number_of_occurrences', 'displayed_depressive_symptoms',
                  'frustration_tolerance_number_of_occurrences', 'demonstrated_anxiety')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PsychoSocialSkillsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-psychosocialgoals'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_pssgoals/#psychosocialskills'
        self.helper.add_input(Submit('submit', 'Submit'))

        if user:
            user_goals = Goals.get_psycho_social_goals(user)
            if Goals.PSS_RANGE_OF_AFFECT not in user_goals:
                del self.fields['smiled']
                del self.fields['frowned']
            if Goals.PSS_SELF_ESTEEM not in user_goals:
                del self.fields['made_negative_comments_self']
                del self.fields['made_positive_comments_self']
            if Goals.PSS_LEADERSHIP not in user_goals:
                del self.fields['refused_to_lead_activity']
                del self.fields['lead_activity']
            if Goals.PSS_RESTLESSNESS not in user_goals:
                del self.fields['left_program']
            if Goals.PSS_PAIN_MANAGMENT not in user_goals:
                del self.fields['complained_of_pain']
            if Goals.PSS_DECREASE_COMPULSIVE not in user_goals:
                del self.fields['destructive_behaviour_number_of_occurrences']
            if Goals.PSS_DECREASE_DEPRESSIVE:
                del self.fields['displayed_depressive_symptoms']
            if Goals.PSS_INCREASE_TOLERANCE:
                del self.fields['frustration_tolerance_number_of_occurrences']
            if Goals.PSS_INCREASE_ANXIETY_CONTROL:
                del self.fields['demonstrated_anxiety']


class MotorSkillsAssessmentForm(ModelForm):
    class Meta:
        model = MotorSkillsAssessment
        fields = ('independent_mobility', 'gait', 'endurance', 'structure_dance', 'grasped_instruments_mallets',
                  'demonstrated_finger_independence', 'turn_pages_of_songbook', 'demonstrated_upper_extremity_control',
                  'range_of_motion', 'crosses_midline', 'reach_for_instrument', 'demonstrates_adequate_eye_hand_coordination',
                  'demonstrated_adequate_body_coordination', 'full_hearing', 'full_sight')

    def __init__(self, *args, **kwargs):
        super(MotorSkillsAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-motorassessment'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_motorassess/#motorskills'
        self.helper.add_input(Submit('submit', 'Submit Skills Assessment'))
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Motor Skills Assessment',
                               'independent_mobility', 'gait', 'endurance', 'structure_dance', 'grasped_instruments_mallets',
                               'demonstrated_finger_independence', 'turn_pages_of_songbook', 'demonstrated_upper_extremity_control',
                               'range_of_motion', 'crosses_midline', 'reach_for_instrument', 'demonstrates_adequate_eye_hand_coordination',
                               'demonstrated_adequate_body_coordination', 'full_hearing', 'full_sight')
            )
        )


class MotorSkillsForm(ModelForm):
    class Meta:
        model = MotorSkillsGoals
        fields = ('mobility_activity', 'fine_motor_activity', 'gross_motor_activity', 'coordination_activity')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MotorSkillsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-motorgoals'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_motorgoals/#motorskills'
        self.helper.add_input(Submit('submit', 'Submit'))

        if user:
            user_goals = Goals.get_motor_goals(user)
            if Goals.MTR_FINE not in user_goals:
                del self.fields['fine_motor_activity']
            if Goals.MTR_MOBILITY not in user_goals:
                del self.fields['mobility_activity']
            if Goals.MTR_GROSS not in user_goals:
                del self.fields['gross_motor_activity']
            if Goals.MTR_COORDINATION not in user_goals:
                del self.fields['coordination_activity']


class CognitiveSkillsAssessmentForm(ModelForm):
    class Meta:
        model = CognitiveMemorySkillsAssessment
        fields = ('recalls_own_name', 'recalls_name_familiar_persons', 'recalls_melody_familiar_songs', 'recalls_lyrics_familiar_songs', 'play_instruments',
                  'recognize_error_self_correct', 'read_song_sheet_book', 'organize_thoughts', 'remains_on_task', 'starts_stops_correct', 'maintains_synchrony_with_another',
                  'follow_verbal_directions', 'follow_non_verbal_directions', 'follows_hand_over_hand_directions', 'long_term_memory', 'short_term_memory', 'oriented_time',
                  'oriented_place')

    def __init__(self, *args, **kwargs):
        super(CognitiveSkillsAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-cogassessment'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_cogassess/#cognitiveskills'
        self.helper.add_input(Submit('submit', 'Submit Skills Assessment'))
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Cognitive Skills Assessment',
                               'recalls_own_name', 'recalls_name_familiar_persons', 'recalls_melody_familiar_songs', 'recalls_lyrics_familiar_songs', 'play_instruments',
                               'recognize_error_self_correct', 'read_song_sheet_book', 'organize_thoughts', 'remains_on_task', 'starts_stops_correct', 'maintains_synchrony_with_another',
                               'follow_verbal_directions', 'follow_non_verbal_directions', 'follows_hand_over_hand_directions', 'long_term_memory', 'short_term_memory',
                               'oriented_time', 'oriented_place')
            )
        )


class CognitiveSkillsForm(ModelForm):
    class Meta:
        model = CognitionMemorySkillsGoals
        fields = ('choice_made_verbally', 'choice_made_nonverbally', 'reaction_to_vocal_stimuli', 'reaction_to_recorded_stimuli', 'reactions_to_instrumental_stimuli', 'questions_were_answered',
                  'long_term_memory_retrieved', 'short_term_memory_retrieved', 'occurrences_confusion_disorientation', 'willing_participation', 'encouraged_participation')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CognitiveSkillsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-coggoals'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_coggoals/#cognitiveskills'
        self.helper.add_input(Submit('submit', 'Submit'))

        if user:
            user_goals = Goals.get_cognitive_memory_goals(user)
            if Goals.COG_CHOICE_MAKING not in user_goals:
                del self.fields['choice_made_verbally']
                del self.fields['choice_made_nonverbally']
            if Goals.COG_SENSORY_STIMULATION not in user_goals:
                del self.fields['reaction_to_vocal_stimuli']
                del self.fields['reaction_to_recorded_stimuli']
                del self.fields['reactions_to_instrumental_stimuli']
            if Goals.COG_MAINTAIN_FUNCTION not in user_goals:
                del self.fields['questions_were_answered']
                del self.fields['long_term_memory_retrieved']
                del self.fields['short_term_memory_retrieved']
            if Goals.COG_DECREASE_CONFUSION not in user_goals:
                del self.fields['occurrences_confusion_disorientation']
            if Goals.COG_INCREASE_LEVEL_PART not in user_goals:
                del self.fields['willing_participation']
                del self.fields['encouraged_participation']