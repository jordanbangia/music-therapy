from django.contrib import admin

from .models import UserInfo
from .models import MusicalPreference
from .models import CommunicationGoalsUpdate, InitialCommunicationSkills
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(MusicalPreference)
admin.site.register(CommunicationGoalsUpdate)
admin.site.register(InitialCommunicationSkills)