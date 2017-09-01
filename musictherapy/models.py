from django.core import exceptions
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

SKILLS_SCALE = (
    (-1, 'Not Measured'),
    (0, 'None/ Never'),
    (1, 'Low/ Rarely'),
    (2, 'Medium/ Sometimes'),
    (3, 'High/ Always')
)

LOCATION_CHOICES = (
    ('Brampton', 'Brampton'),
    ('Brunel', 'Brunel'),
    ('Meadowvale', 'Meadowvale'),
    ('Sam McCallion', 'Sam McCallion'),
    ('Evelyn\'s', 'Evelyn\'s')
)

PROGRAM_DATES = (
    ('1', 'September - February'),
    ('2', 'March - August')
)

DAYS_OF_WEEK = (
    ('mon', 'Monday'),
    ('tue', 'Tuesday'),
    ('wed', 'Wednesday'),
    ('thu', 'Thursday'),
    ('fri', 'Friday'),
    ('sat', 'Saturday'),
    ('sun', 'Sunday')
)


class Program(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    date = models.CharField(max_length=1, verbose_name="Program Dates", choices=PROGRAM_DATES)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, verbose_name="Location", null=True, blank=True)
    day_of_week = models.CharField(max_length=3, verbose_name="Day of Week", choices=DAYS_OF_WEEK, null=True, blank=True)
    time = models.TimeField(verbose_name="Time", null=True, blank=True)
    description = models.TextField(default="", verbose_name="Description", null=True, blank=True)

    class Meta:
        unique_together = ('name', 'date', 'day_of_week', 'location', 'time')

    def __unicode__(self):
        return ', '.join([str(field) for field in
                         [self.location, self.name, self.get_date_display(), self.get_day_of_week_display(), self.time]
                         if field is not None])


class UserInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    location = MultiSelectField(max_length=100, choices=LOCATION_CHOICES, verbose_name="Location")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    diagnosis = models.CharField(max_length=500, blank=True, verbose_name="Diagnosis")
    history = models.TextField(verbose_name="Life Experiences/History")
    country_of_origin = models.CharField(max_length=100, verbose_name="Country of Origin")
    language_spoken = models.CharField(max_length=100, verbose_name="Language Spoken")
    musical_history = models.CharField(max_length=500, verbose_name="Musical History")
    care_plan = models.TextField(default="", verbose_name="Alzheimer Society Peel Care Plan")
    program = models.ManyToManyField(Program, blank=True)
    asp_level = models.IntegerField(verbose_name="Alzheimer Society Peel Level of Care", choices=((1, 1), (2, 2), (3, 3)))
    updated = models.DateTimeField(auto_now=True)
    active = models.IntegerField(choices=((0, 'archived'), (1, 'active')), default=1)

    def __unicode__(self):
        return self.name


class Session(models.Model):
    STATUS_CHOICES = (
        (0, 'Missed'),
        (1, 'Attended')
    )

    user = models.ForeignKey(UserInfo, related_name="sessions", null=False)
    date = models.DateField(verbose_name="Session Date")
    note = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def save(self, *args, **kwargs):
        # On create, set the date if one isn't provided
        if not self.id and not self.date:
            self.date = timezone.now().date()
        return super(Session, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('user', 'date')

    def __unicode__(self):
        return '{}-{}-{}'.format(self.user.name, self.date, self.date)


class Domains(models.Model):
    name = models.CharField(max_length=100, null=False)
    enabled = models.IntegerField(choices=((0, 'Disabled'), (1, 'Enabled')))
    parent = models.ForeignKey('self', related_name="subcategories", null=True, blank=True)

    class Meta:
        verbose_name = 'Domain'

    def __unicode__(self):
        return self.name if not self.parent else '{} - {}'.format(self.parent.name, self.name)


class Goals(models.Model):
    domain = models.ForeignKey(Domains, related_name="goals", null=True)
    name = models.CharField(max_length=100, null=False)
    parent = models.ForeignKey('self', related_name="subgoals", null=True, blank=True)
    enabled = models.IntegerField(choices=((0, 'Disabled'), (1, 'Enabled')))
    is_custom = models.IntegerField(choices=((0, 'Not Custom'), (1, 'Custom')), default=0)
    user = models.ForeignKey(UserInfo, null=True, blank=True)

    class Meta:
        verbose_name = 'Goal'

    def __unicode__(self):
        return '{} - {}'.format(self.domain.name, self.name)


class DomainMeasurables(models.Model):
    domain = models.ForeignKey(Domains, related_name="domainmeasurables", null=False)
    pos_neg = models.IntegerField(choices=((1, 'Positive'), (-1, 'Negative')), null=False)
    name = models.CharField(max_length=300, null=False)
    enabled = models.IntegerField(choices=((0, 'Disabled'), (1, 'Enabled')))

    class Meta:
        verbose_name = 'Domain Measurable'

    def __unicode__(self):
        return '{} - {}'.format(self.domain.name, self.name)


class GoalsMeasurables(models.Model):
    goal = models.ForeignKey(Goals, related_name="goalsmeasurables", null=True, blank=True)
    name = models.CharField(max_length=300, null=False)
    enabled = models.IntegerField(choices=((0, 'Disabled'), (1, 'Enabled')))
    is_custom = models.IntegerField(choices=((0, 'Not Custom'), (1, 'Custom')), default=0)
    user = models.ForeignKey(UserInfo, null=True, blank=True)

    class Meta:
        verbose_name = 'Goal Measurable'

    def __unicode__(self):
        return '{} - {} - {}'.format(self.goal.domain.name, self.goal.name, self.name)


class UserMeasurables(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="measurables", null=False)
    measurable = models.ForeignKey(DomainMeasurables, on_delete=models.CASCADE, null=False)
    value = models.IntegerField(choices=SKILLS_SCALE)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'measurable', 'updated')


class UserDomainNoteMeasurables(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="measurables_note", null=False)
    domain = models.ForeignKey(Domains, related_name="domainmeasurablesnote", null=False)
    note = models.TextField(default="", null=True, blank=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'domain', 'updated')


class UserGoals(models.Model):
    user = models.ForeignKey(UserInfo, null=False)
    goal = models.ForeignKey(Goals, on_delete=models.CASCADE, null=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'goal')


class UserGoalMeasurables(models.Model):
    goal_measurable = models.ForeignKey(GoalsMeasurables, on_delete=models.CASCADE, null=True)
    session = models.ForeignKey(Session, null=True)
    value = models.IntegerField(choices=SKILLS_SCALE)
    updated = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.goal_measurable.name, self.session.id, self.session.user.name)

    # class Meta:
    #     unique_together = ('user', 'goal_measurable', 'updated', 'session')


class UserGoalNoteMeasurable(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="goalmeasurables_note", null=True)
    session = models.ForeignKey(Session, null=True)
    domain = models.ForeignKey(Domains, null=False)
    note = models.TextField(default="", null=True, blank=True)
    updated = models.DateTimeField(blank=True, null=True)
    #
    # class Meta:
    #     unique_together = ('user', 'domain', 'updated', 'session')


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
        ('Rock \'n\' Roll', 'Rock \'n\' Roll'),
        ('Motown', 'Motown'),
        ('Jazz', 'Jazz'),
        ('Marching Band', 'Marching Band'),
        ('Meditative', 'Meditative'),
        ('Musical TV Shows', 'Musical TV Shows'),
        ('Ragtime', 'Ragtime'),
        ('Pop Music', 'Pop Music'),
        ('Rhythm and Blues', 'Rhythm and Blues'),
        ('Soul', 'Soul'),
        ('Patriotic', 'Patriotic'),
    )

    user = models.OneToOneField(UserInfo, primary_key=True)
    fav_composer = models.CharField(max_length=200, null=True, blank=True, verbose_name="Favourite Composer/Performer(s)")
    fav_song = models.CharField(max_length=200, null=True, blank=True, verbose_name="Favourite Song(s)")
    fav_instrument = models.CharField(max_length=200, null=True, blank=True, verbose_name="Favourite Instrument(s)")
    preferred_style = MultiSelectField(choices=STYLES_CHOICES, null=True, blank=True)
    other_style = models.CharField(max_length=200, null=True, blank=True)
    ethnic = models.CharField(max_length=200, null=True, blank=True)
    sacred_music = models.CharField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
