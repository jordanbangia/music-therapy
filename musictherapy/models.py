from django.db import models
from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

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

class InitialCommunicationSkills(models.Model):
    user = models.OneToOneField(UserInfo, primary_key=True)

    #verbal skills
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
    follow_directions = models.IntegerField(choices=SKILLS_SCALE)
    response_to_verbal_instr = models.IntegerField(choices=SKILLS_SCALE)
    respond_to_name_song = models.IntegerField(choices=SKILLS_SCALE)
    respond_to_hello_goodbye = models.IntegerField(choices=SKILLS_SCALE)

    #singing/vocal skills
    call_and_response = models.IntegerField(choices=SKILLS_SCALE)
    singing_familiar_songs = models.IntegerField(choices=SKILLS_SCALE)

    #vocalization
    sing_familiar_songs_syllables = models.IntegerField(choices=SKILLS_SCALE)

    #interactive speech
    greet_others = models.IntegerField(choices=SKILLS_SCALE)

    #choice making
    make_choice_in_song = models.IntegerField(choices=SKILLS_SCALE)

class CommunicationGoalsUpdate(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #increase level of communication
    verbal_part_with_verbal_prompt = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    verbal_part_without_verbal_prompt = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    #increase self-expression
    feelings_were_articulated = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    opinions_given = models.PositiveIntegerField(validators=[MaxValueValidator(10)])