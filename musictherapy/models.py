from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

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
		#ethnic, sacred, other
	)

	user = models.ForeignKey(UserInfo)
	fav_composer = models.CharField(max_length=200)
	fav_song = models.CharField(max_length=200)
	fav_instrument = models.CharField(max_length=200)
	preferred_style = MultiSelectField(choices=STYLES_CHOICES, null=True, blank=True)

