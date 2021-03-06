from datetime import date

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ChoiceField, IntegerField, CheckboxSelectMultiple

import musictherapy.models as models
from musictherapy.extras import SelectDateWidget, BirthDateWidget


class ProgramForm(ModelForm):
    class Meta:
        model = models.Program
        fields = ('name', 'location', 'date', 'day_of_week', 'time', 'description')

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-programform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-6'
        self.helper.form_post = 'post'
        self.helper.form_action = reverse('musictherapy:save_program')
        self.helper.form_tag = False
        # self.helper.add_input(Submit('submit', 'Save'))


class SessionForm(ModelForm):
    class Meta:
        model = models.Session
        fields = ('date',)
        widgets = {
            'date': SelectDateWidget
        }

    def __init__(self, *args, **kwargs):
        super(SessionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-createsessionform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-6'
        self.helper.form_post = 'post'
        if self.instance.user is not None:
            self.helper.form_action = reverse('musictherapy:create_session', kwargs={'user_id': int(self.instance.user.pk)})
        self.helper.add_input(Submit('submit', 'Create'))


class UserInfoForm(ModelForm):
    age = IntegerField(label="Age", required=False)

    class Meta:
        model = models.UserInfo
        fields = ('name', 'location', 'date_of_birth', 'age', 'diagnosis', 'history', 'country_of_origin', 'language_spoken',
                  'musical_history', 'care_plan', 'asp_level', 'program')
        widgets = {
            'date_of_birth': BirthDateWidget,
            'program': CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        today = date.today()
        born = kwargs['instance'].date_of_birth if 'instance' in kwargs and hasattr(kwargs['instance'], 'date_of_birth') else None
        if born:
            self.fields['age'].initial = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        self.fields['program'].queryset = models.Program.objects.order_by('location', 'name')
        self.helper = FormHelper()

        self.helper.form_id = 'id-userinfoform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_tag = False


class MusicalPrefForm(ModelForm):
    class Meta:
        model = models.MusicalPreference
        fields = ('fav_composer', 'fav_song', 'fav_instrument', 'preferred_style', 'ethnic', 'sacred_music', 'other_style')

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        super(MusicalPrefForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_id = 'id-musicalprefform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_action = reverse('musictherapy:save_musicpref', kwargs={'user_id': int(user_id)})
        self.helper.add_input(Submit('submit', 'Save'))


class StaffForm(UserCreationForm):
    staff_status = ChoiceField(choices=(('Admin', 'Admin'), ('Staff', 'Staff')),
                               required=True,
                               label='Staff level',
                               initial='Admin')


class SessionStatusForm(ModelForm):
    class Meta:
        model = models.Session
        fields = ('status', 'note')

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id')
        session_id = kwargs.pop('session_id')
        super(SessionStatusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-sessionstatusform'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_post = 'post'
        self.helper.form_tag = False
        self.helper.form_action = reverse('musictherapy:save_session_status', kwargs={'user_id': int(user_id), 'session_id': int(session_id)})
        # self.helper.add_input(Submit('submit', 'Save'))
