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

class PsychoSocialAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    mood_affect = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    display_range_of_affect = models.IntegerField(choices=SKILLS_SCALE)
    self_esteem_confidence = models.IntegerField(choices=SKILLS_SCALE)
    sense_of_humour = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurables(self):
        self.mood_affect = 100 * float(self.display_range_of_affect + self.self_esteem_confidence +
                                       self.sense_of_humour) / float(3 * 3)
        self.total = self.mood_affect

class PsychoSocialGoals(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #increase range of affect
    smiled = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    frowned = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase self-esteem
    made_negative_comments_self = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    made_positive_comments_self = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase leadership role
    refused_to_lead_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    lead_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #decrease restlessness
    left_program = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase pain management
    complained_of_pain = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #decrease compulsive/destructive behaviour
    destructive_behaviour_number_of_occurrences = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #decrease depressive symptoms
    displayed_depressive_symptoms = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase frustration tolerance
    depressive_symptoms_number_of_occurences = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase frustration tolerance
    frustration_tolerance_number_of_occurences = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #decrease level of anxiety
    demonstrated_anxiety = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

class MotorSkillsAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    mobility = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    independent_mobility = models.IntegerField(choices=SKILLS_SCALE)
    gait = models.IntegerField(choices=SKILLS_SCALE)
    endurance = models.IntegerField(choices=SKILLS_SCALE)
    structure_dance = models.IntegerField(choices=SKILLS_SCALE)

    fine_motor = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    grasped_instruments_mallets = models.IntegerField(choices=SKILLS_SCALE)
    demonstrated_finger_independence = models.IntegerField(choices=SKILLS_SCALE)
    turn_pages_of_songbook = models.IntegerField(choices=SKILLS_SCALE)

    gross_motor = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    demonstrated_upper_extremity_control = models.IntegerField(choices=SKILLS_SCALE)
    range_of_motion = models.IntegerField(choices=SKILLS_SCALE)
    crosses_midline = models.IntegerField(choices=SKILLS_SCALE)
    reach_for_instrument = models.IntegerField(choices=SKILLS_SCALE)

    coordination = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    demonstrates_adequate_eye_hand_coordination = models.IntegerField(choices=SKILLS_SCALE)
    demonstrated_adequate_body_coordination = models.IntegerField(choices=SKILLS_SCALE)

    limitations = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    full_hearing = models.IntegerField(choices=SKILLS_SCALE)
    full_sight = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurables(self):
        self.mobility = 100 * float(self.independent_mobility + self.gait + self.endurance +
                                    self.structure_dance) / float(4 * 3)
        self.fine_motor = 100 * float(self.grasped_instruments_mallets + self.demonstrated_finger_independence +
                                      self.turn_pages_of_songbook) / float(3 * 3)
        self.gross_motor = 100 * float(self.demonstrated_upper_extremity_control + self.range_of_motion +
                                       self.crosses_midline + self.reach_for_instrument) / float(4 * 3)
        self.coordination = 100 * float(self.demonstrated_adequate_body_coordination +
                                        self.demonstrates_adequate_eye_hand_coordination) / float(2 * 3)
        self.limitations = 100 * float(self.full_hearing + self.full_sight) / float(2 * 3)
        self.total = float(self.mobility + self.fine_motor + self.gross_motor +
                           self.coordination + self.limitations) / float(5)

class MotorSkillsGoals(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #stimulate and maintain mobility
    mobility_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #stimulate and maintain fine motor skills
    fine_motor_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #stimulate and maintain gross motor skills
    gross_motor_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #stimulate and maintain coordination
    coordination_activity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

class CognitiveMemorySkillsAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    cognition = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    recalls_own_name = models.IntegerField(choices=SKILLS_SCALE)
    recalls_name_familiar_persons = models.IntegerField(choices=SKILLS_SCALE)
    recalls_melody_familiar_songs = models.IntegerField(choices=SKILLS_SCALE)
    recalls_lyrics_familiar_songs = models.IntegerField(choices=SKILLS_SCALE)
    play_instruments = models.IntegerField(choices=SKILLS_SCALE)
    recognize_error_self_correct = models.IntegerField(choices=SKILLS_SCALE)
    read_song_sheet_book = models.IntegerField(choices=SKILLS_SCALE)
    organize_thoughts = models.IntegerField(choices=SKILLS_SCALE)
    remains_on_task = models.IntegerField(choices=SKILLS_SCALE)
    starts_stops_correct = models.IntegerField(choices=SKILLS_SCALE)
    maintains_synchrony_with_another = models.IntegerField(choices=SKILLS_SCALE)
    follow_verbal_directions = models.IntegerField(choices=SKILLS_SCALE)
    follow_non_verbal_directions = models.IntegerField(choices=SKILLS_SCALE)
    follows_hand_over_hand_directions = models.IntegerField(choices=SKILLS_SCALE)

    memory = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    long_term_memory = models.IntegerField(choices=SKILLS_SCALE)
    short_term_memory = models.IntegerField(choices=SKILLS_SCALE)
    oriented_time = models.IntegerField(choices=SKILLS_SCALE)
    oriented_place = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurables(self):
        self.cognition = 100 * float(self.recalls_own_name + self.recalls_name_familiar_persons +
                                     self.recalls_melody_familiar_songs + self.recalls_lyrics_familiar_songs +
                                     self.play_instruments + self.recognize_error_self_correct +
                                     self.read_song_sheet_book + self.organize_thoughts + self.remains_on_task +
                                     self.starts_stops_correct + self.maintains_synchrony_with_another +
                                     self.follow_verbal_directions + self.follow_non_verbal_directions +
                                     self.follows_hand_over_hand_directions) / float(14 * 4)
        self.memory = 100 * float(self.long_term_memory + self.short_term_memory + self.oriented_time +
                                  self.oriented_place) / float(4 * 3)

class CognitionMemorySkillsGoalsMeasurables(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #increase choice making
    choice_made_verbally = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    choice_made_nonverbally = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase sensory stimulation
    reaction_to_vocal_stimuli = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    reaction_to_recorded_stimuli = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    reactions_to_instrumental_stimuli = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #maintain cognitive function
    questions_were_answered = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    long_term_memory_retrieved = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    short_term_memory_retrieved = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #decrease confusion and disorientation
    occurrences_confusion_disorientation = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    #increase level of participation
    willing_participation = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    encouraged_participation = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

