from .models import UserInfo, MusicalPreference, InitialCommunicationSkills, CommunicationGoalsUpdate
from .extras import SelectDateWidget
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Accordion, AccordionGroup

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

class InitialCommunicationAssessmentForm(ModelForm):
    class Meta:
        model = InitialCommunicationSkills
        fields = ('verbalize_choices', 'fill_in_the_blank', 'engage_in_conv', 'answer_questions', 'song_writing',
                  'communicated_with_single_words', 'communicated_with_phrases', 'communicated_with_sentences',
                  'disjointed_response', 'appropriate_rate_of_speech', 'word_finding_difficulty', 'imitate_therapist',
                  'follow_directions', 'response_to_verbal_instr', 'respond_to_name_song', 'respond_to_hello_goodbye',
                  'call_and_response', 'singing_familiar_songs', 'sing_familiar_songs_syllables', 'greet_others',
                  'make_choice_in_song')

    def __init__(self, *args, **kwargs):
        super(InitialCommunicationAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-initialcomskills'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_initialcomskills/#communicationskills'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup('Verbal Skills',
                               'verbalize_choices', 'fill_in_the_blank', 'engage_in_conv', 'answer_questions',
                               'song_writing', 'communicated_with_single_words', 'communicated_with_phrases',
                               'communicated_with_sentences', 'disjointed_response', 'appropriate_rate_of_speech',
                               'word_finding_difficulty', 'imitate_therapist'),
                AccordionGroup('Receptive Language',
                               'follow_directions', 'response_to_verbal_instr', 'respond_to_name_song',
                               'respond_to_hello_goodbye'),
                AccordionGroup('Singing/Vocal Skills',
                               'call_and_response', 'singing_familiar_songs'),
                AccordionGroup('Vocalization',
                               'sing_familiar_songs_syllables'),
                AccordionGroup('Interactive Speech',
                               'greet_others'),
                AccordionGroup('Choice Making',
                               'make_choice_in_song')
            )
        )

class CommunicationSkillsForm(ModelForm):
    class Meta:
        model = CommunicationGoalsUpdate
        fields = ('verbal_part_with_verbal_prompt', 'verbal_part_without_verbal_prompt', 'feelings_were_articulated',
                  'opinions_given')

    def __init__(self, *args, **kwargs):
        super(CommunicationSkillsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-communicationskills'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = 'submit_communicationskillsupdate/#communicationskills'
        self.helper.add_input(Submit('submit', 'Submit'))