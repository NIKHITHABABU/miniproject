# admin.py
from django.contrib import admin
from .models import Registers, Grievance,feedbackforms,Appeal

admin.site.register(Registers)
admin.site.register(Grievance)
admin.site.register(feedbackforms)
admin.site.register(Appeal)

