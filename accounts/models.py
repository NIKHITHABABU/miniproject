from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
