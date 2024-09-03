# models.py
from django.db import models

class Registers(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mail = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Grievance(models.Model):
    GRIEVANCE_CHOICES = [
        ('academic', 'Academic'),
        ('administrative', 'Administrative'),
        ('others', 'Others'),
    ]

    complaint_title = models.CharField(max_length=255)
    type_of_grievance = models.CharField(max_length=50, choices=GRIEVANCE_CHOICES)
    complaint_description = models.TextField()

    def __str__(self):
        return self.complaint_title
