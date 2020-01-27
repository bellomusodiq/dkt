from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(UserType)
admin.site.register(Profile)
admin.site.register(AllergiesReaction)
admin.site.register(Meditation)
admin.site.register(PersonalDoctor)
admin.site.register(EmergencyContact)
admin.site.register(Checkup)