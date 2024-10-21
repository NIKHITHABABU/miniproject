# admin.py
from django.contrib import admin
from .models import Registers, Grievance,feedbackforms,Appeal

admin.site.register(Registers)
admin.site.register(Grievance)
admin.site.register(feedbackforms)
admin.site.register(Appeal)

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'description', 'date']
