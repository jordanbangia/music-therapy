from django.contrib import admin

from .models import UserInfo
from .models import MusicalPreference
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(MusicalPreference)
