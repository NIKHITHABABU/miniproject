# admin.py
from django.contrib import admin
from .models import Registers, Grievance

admin.site.register(Registers)
admin.site.register(Grievance)
