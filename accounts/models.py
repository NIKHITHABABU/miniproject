from django.db import models

# Create your models here.
class Registers(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname