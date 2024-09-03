# admin.py
from django.contrib import admin
from .models import Registers, Grievance,feedbackforms

admin.site.register(Registers)
admin.site.register(Grievance)
admin.site.register(feedbackforms)