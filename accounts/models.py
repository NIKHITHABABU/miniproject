from django.db import models

# Create your models here.
class Registers(models.Model):
    name = models.CharField(max_length=100)
    # lname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    # phone = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class complaints(models.Model):
    ctitle = models.CharField(max_length=100)
    # lname = models.CharField(max_length=100)
    ctype = models.CharField(max_length=100)
    # phone = models.IntegerField()
    cdescription = models.CharField(max_length=120)
    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.ctitle