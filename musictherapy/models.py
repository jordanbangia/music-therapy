from django.db import models
from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

from goals import Goals

# Create your models here.
NONE = 0
LOW = 1
MEDIUM = 2
HIGH = 3
SKILLS_SCALE = {
    (NONE, 'None/ Never'),
    (LOW, 'Low/ Rarely'),
    (MEDIUM, 'Medium/ Sometimes'),
    (HIGH, 'High/ Always')
}

class UserInfo(models.Model):
    LOCATION_CHOICES = (
        ('Brampton', 'Brampton'),
        ('Brunel', 'Brunel'),
        ('Meadowvale', 'Meadowvale'),
        ('Sam McCallion', 'Sam McCallion'),
        ('Evelyn\'s', 'Evelyn\'s')
    )

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    date_of_birth = models.DateField('DOB')
    diagnosis = models.CharField(max_length=300, blank=True)
    history = models.CharField(max_length=300)
    country_of_origin = models.CharField(max_length=100)
    language_spoken = models.CharField(max_length=100)
    musical_history = models.CharField(max_length=500)
    care_plan = models.CharField(max_length=200)
    asp_level = models.IntegerField()
    goals = MultiSelectField(choices=Goals.GOALS_CHOICES, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class MusicalPreference(models.Model):
    STYLES_CHOICES = (
        ('Big Band', 'Big Band'),
        ('Broadway/Movie Musicals', 'Broadway/Movie Musicals'),
        ('Classical Instrumental', 'Classical Instrumental'),
        ('Classical Vocal', 'Classical Vocal'),
        ('Easy Listening', 'Easy Listening'),
        ('Folk', 'Folk'),
        ('Bluegrass', 'Bluegrass'),
        ('Gospel', 'Gospel'),
        ('Opera', 'Opera'),
        ('Country and Western', 'Country and Western'),
        ('Heavy Rock', 'Heavy Rock'),
        ('Electronic', 'Electronic'),
        ('Jazz', 'Jazz'),
        ('Marching Band', 'Marching Band'),
        ('Meditative', 'Meditative'),
        ('Musical TV Shows', 'Musical TV Shows'),
        ('Ragtime', 'Ragtime'),
        ('Pop Music', 'Pop Music'),
        ('Rhythm and Blues', 'Rhythm and Blues'),
        ('Soul', 'Soul'),
        ('Patriotic', 'Patriotic'),
        # ethnic, sacred, other
    )

    user = models.OneToOneField(UserInfo, primary_key=True)
    fav_composer = models.CharField(max_length=200)
    fav_song = models.CharField(max_length=200)
    fav_instrument = models.CharField(max_length=200)
    preferred_style = MultiSelectField(choices=STYLES_CHOICES, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

class CommunicationAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    #verbal skills
    verbal_skills = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    verbalize_choices = models.IntegerField(choices=SKILLS_SCALE)
    fill_in_the_blank = models.IntegerField(choices=SKILLS_SCALE)
    engage_in_conv = models.IntegerField(choices=SKILLS_SCALE)
    answer_questions = models.IntegerField(choices=SKILLS_SCALE)
    song_writing = models.IntegerField(choices=SKILLS_SCALE)
    communicated_with_single_words = models.IntegerField(choices=SKILLS_SCALE)
    communicated_with_phrases = models.IntegerField(choices=SKILLS_SCALE)
    communicated_with_sentences = models.IntegerField(choices=SKILLS_SCALE)
    disjointed_response = models.IntegerField(choices=SKILLS_SCALE)
    appropriate_rate_of_speech = models.IntegerField(choices=SKILLS_SCALE)
    word_finding_difficulty = models.IntegerField(choices=SKILLS_SCALE)
    imitate_therapist = models.IntegerField(choices=SKILLS_SCALE)

    #receptive language
    receptive_language = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    follow_directions = models.IntegerField(choices=SKILLS_SCALE)
    response_to_verbal_instr = models.IntegerField(choices=SKILLS_SCALE)
    respond_to_name_song = models.IntegerField(choices=SKILLS_SCALE)
    respond_to_hello_goodbye = models.IntegerField(choices=SKILLS_SCALE)

    #singing/vocal skills
    singing_vocal_skills = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    call_and_response = models.IntegerField(choices=SKILLS_SCALE)
    singing_familiar_songs = models.IntegerField(choices=SKILLS_SCALE)

    #vocalization
    vocalization = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    sing_familiar_songs_syllables = models.IntegerField(choices=SKILLS_SCALE)

    #interactive speech
    interactive_speech = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    greet_others = models.IntegerField(choices=SKILLS_SCALE)

    #choice making
    choice_making = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    make_choice_in_song = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurables(self):
        self.verbal_skills = 100 * float(self.verbalize_choices + self.fill_in_the_blank + self.engage_in_conv +
                                   self.answer_questions + self.song_writing + self.communicated_with_single_words +
                                   self.communicated_with_phrases + self.communicated_with_sentences +
                                   self.disjointed_response + self.appropriate_rate_of_speech +
                                   self.word_finding_difficulty + self.imitate_therapist) / float(12 * 3)
        self.receptive_language = 100 * float(self.follow_directions + self.response_to_verbal_instr +
                                             self.respond_to_name_song + self.respond_to_hello_goodbye) / float(4 * 3)
        self.singing_vocal_skills = 100 * float(self.call_and_response + self.singing_familiar_songs) / float(2 * 3)
        self.vocalization = 100 * float(self.sing_familiar_songs_syllables) / float(1 * 3)
        self.interactive_speech = 100 * float(self.greet_others) / float(1 * 3)
        self.choice_making = 100 * float(self.make_choice_in_song) / float(1 * 3)

        self.total = float(self.verbal_skills + self.receptive_language + self.singing_vocal_skills + self.vocalization
                           + self.interactive_speech + self. choice_making) / float(6)


class CommunicationGoals(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #increase level of communication
    verbal_part_with_verbal_prompt = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    verbal_part_without_verbal_prompt = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase self-expression
    feelings_were_articulated = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    opinions_given = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)