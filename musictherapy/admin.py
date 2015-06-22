from django.contrib import admin

from .models import UserInfo
from .models import MusicalPreference
from .models import CommunicationGoals, CommunicationAssessment
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(MusicalPreference)
admin.site.register(CommunicationGoals)
admin.site.register(CommunicationAssessment)