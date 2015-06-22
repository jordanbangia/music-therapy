from .models import UserInfo, MusicalPreference, CommunicationAssessment, CommunicationGoals
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
            print(user_goals)
            if Goals.COM_INCREASE_LEVEL not in user_goals:
                del self.fields['verbal_part_with_verbal_prompt']
                del self.fields['verbal_part_without_verbal_prompt']
            if Goals.COM_INCREASE_SELF_EXPRESSION not in  user_goals:
                del self.fields['feelings_were_articulated']
                del self.fields['opinions_given']