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

class ObservableBehaviours(models.Model):
    BEHAVIOUR_CHOICES = (
        ('Abusive to others (physically)', 'Abusive to others (physically)'),
        ('Abusive to others (verbally)', 'Abusive to others (verbally)'),
        ('Agitation', 'Agitation'),
        ('Amivalent/detached', 'Ambivalent/detached'),
        ('Assertive', 'Assertive'),
        ('Crying', 'Crying'),
        ('Delusions', 'Delusions'),
        ('Depressed', 'Depressed'),
        ('Disruptive', 'Disruptive'),
        ('Exit Seeking', 'Exit Seeking'),
        ('Fearful', 'Fearful'),
        ('Flat affect', 'Flat affect'),
        ('Hallucinations', 'Hallucinations'),
        ('Hoarding', 'Hoarding'),
        ('Impulsive', 'Impulsive'),
        ('Isolative', 'Isolative'),
        ('Labile', 'Labile'),
        ('Manipulative', 'Manipulative'),
        ('Oral Fixation', 'Oral Fixation'),
        ('Passive', 'Passive'),
        ('Physically Perseverative', 'Physically Perseveration'),
        ('Questioning', 'Questioning'),
        ('Repetitive', 'Repetitive'),
        ('Resistive', 'Resistive'),
        ('Restless', 'Restless'),
        ('Self-abusive', 'Self-abusive'),
        ('Self-stimulative', 'Self-stimulative'),
        ('Sleeping', 'Sleeping'),
        ('Territorial', 'Territorial'),
        ('Uncooperative', 'Uncooperative'),
        ('Wanders', 'Wanders'),
        ('Withdrawn', 'Withdrawn')
    )

    user = models.OneToOneField(UserInfo, primary_key=True)
    observable_behaviours = MultiSelectField(choices=BEHAVIOUR_CHOICES, null=True, blank=True)
    obsessions = models.CharField(max_length=400, blank=True, null=True)
    catastrophic_reactions = models.CharField(max_length=400, blank=True, null=True)
    inappropriate_verbal_behaviour = models.CharField(max_length=400, blank=True, null=True)
    inappropriate_nonverbal_behaviour = models.CharField(max_length=400, blank=True, null=True)
    expresses_exhibits_pain = models.CharField(max_length=400, blank=True, null=True)
    comments = models.CharField(max_length=600, blank=True, null=True)

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
    frustration_tolerance_number_of_occurrences = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
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
        self.total = float(self.cognition + self.memory) / float(2)

class CognitionMemorySkillsGoals(models.Model):
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

class SocialSkillsAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    interactions = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    engage_imitation = models.IntegerField(choices=SKILLS_SCALE)
    passing_sharing_instruments = models.IntegerField(choices=SKILLS_SCALE)
    converse_others = models.IntegerField(choices=SKILLS_SCALE)
    dancing_others = models.IntegerField(choices=SKILLS_SCALE)

    attending_skills = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    make_maintain_eye_contact = models.IntegerField(choices=SKILLS_SCALE)
    attend_task = models.IntegerField(choices=SKILLS_SCALE)

    sharing_turn_taking = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    pass_exchange_instrument = models.IntegerField(choices=SKILLS_SCALE)
    play_response_name = models.IntegerField(choices=SKILLS_SCALE)

    participation_group_music = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    active_in_session = models.IntegerField(choices=SKILLS_SCALE)
    remain_in_group = models.IntegerField(choices=SKILLS_SCALE)
    accept_leadership = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurable(self):
        self.interactions = 100 * float(self.engage_imitation + self.passing_sharing_instruments + self.converse_others + self.dancing_others) / float(4 * 3)
        self.attending_skills = 100 * float(self.make_maintain_eye_contact + self.attend_task) / float(2 * 3)
        self.sharing_turn_taking = 100 * float(self.pass_exchange_instrument + self.play_response_name) / float(2 * 3)
        self.participation_group_music = 100 * float(self.active_in_session + self.remain_in_group + self.accept_leadership) /float(3 * 3)
        self.total = float(self.interactions + self.attending_skills + self.sharing_turn_taking + self.participation_group_music) / float(4)

class SocialSkillsGoals(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #increase attention span
    redirection_required = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    encouragement_to_stay_required = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

    #decrease isolation
    participation_in_program = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    joining_of_program = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

    #increase social interaction
    interactions_with_staff = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    interactions_with_peers = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    therapist = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

class MusicSkillsAssessment(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)
    total = models.FloatField(validators=[MaxValueValidator(101)], default = 0)

    rhythm_beat = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    match_rhythm = models.IntegerField(choices=SKILLS_SCALE)
    keep_steady_beat = models.IntegerField(choices=SKILLS_SCALE)
    adapt_to_rhythmic_changes = models.IntegerField(choices=SKILLS_SCALE)

    melody_tonal = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    match_pitch = models.IntegerField(choices=SKILLS_SCALE)
    discriminates_dynamics = models.IntegerField(choices=SKILLS_SCALE)
    discriminates_duration = models.IntegerField(choices=SKILLS_SCALE)
    sing_familiar_songs = models.IntegerField(choices=SKILLS_SCALE)
    finish_musical_phrase = models.IntegerField(choices=SKILLS_SCALE)

    instrument_exploration = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    choose_instrument_play = models.IntegerField(choices=SKILLS_SCALE)

    interest_preference = models.FloatField(validators=[MaxValueValidator(101)], default=0)
    response_to_music = models.IntegerField(choices=SKILLS_SCALE)
    choose_song_style = models.IntegerField(choices=SKILLS_SCALE)
    familiar_song_title_melody = models.IntegerField(choices=SKILLS_SCALE)
    familiar_song_title_lyrics = models.IntegerField(choices=SKILLS_SCALE)

    def fill_measurable(self):
        self.rhythm_beat = 100 * float(self.match_rhythm + self.keep_steady_beat + self.adapt_to_rhythmic_changes) / float(3 * 3)
        self.melody_tonal = 100 * float(self.match_pitch + self.discriminates_dynamics + self.discriminates_duration + self.sing_familiar_songs + self.finish_musical_phrase) / float(5 * 3)
        self.instrument_exploration = 100 * float(self.choose_instrument_play) / float (1 * 3)
        self.interest_preference = 100 * float(self.response_to_music + self.choose_song_style + self.familiar_song_title_lyrics + self.familiar_song_title_melody) / float(4 * 3)
        self.total = float(self.rhythm_beat + self.melody_tonal + self.instrument_exploration + self.interest_preference) / float(4)

class MusicSkillsGoals(models.Model):
    user = models.ForeignKey(UserInfo)
    updated = models.DateTimeField(auto_now=True)

    #maintain current knowledge of music
    music_trivia_answered_correctly = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    song_known_without_lyrics = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    song_known_without_title = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    song_known = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)

    #maintain current music skills
    music_skill_demonstrated = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)
    opinions_given = models.PositiveIntegerField(validators=[MaxValueValidator(10)], blank=True, null=True)