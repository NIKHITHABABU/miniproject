from django.contrib import admin

# Register your models here.
from .models import Registers
from .models import complaints

admin.site.register(Registers) #table registering
admin.site.register(complaints) #complaint table registering

