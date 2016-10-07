from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.forms import ModelForm, ChoiceField, IntegerField

from musictherapy.extras import SelectDateWidget
from musictherapy.models import UserInfo, MusicalPreference
from datetime import date


class UserInfoForm(ModelForm):
    age = IntegerField(label="Age")

    class Meta:
        model = UserInfo
        fields = ('name', 'location', 'date_of_birth', 'age', 'diagnosis', 'history', 'country_of_origin', 'language_spoken',
                  'musical_history', 'care_plan', 'asp_level', 'program')
        widgets = {
            'date_of_birth': SelectDateWidget
        }

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        today = date.today()
        born = kwargs['instance'].date_of_birth
        self.fields['age'].initial = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
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
        fields = ('fav_composer', 'fav_song', 'fav_instrument', 'preferred_style', 'other_style')

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


class StaffForm(UserCreationForm):
    staff_status = ChoiceField(choices=(('Admin', 'Admin'), ('Staff', 'Staff')),
                               required=True,
                               label='Staff level',
                               initial='Admin')

    def save(self, commit=True):
        user = super(StaffForm, self).save(commit=commit)

        if self.cleaned_data.get('staff_status') == 'Admin':
            user.groups.add(Group.objects.get(name='Admin'))
        else:
            user.groups.add(Group.objects.get(name='Staff'))
        user.save()
        return user
