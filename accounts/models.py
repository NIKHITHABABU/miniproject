# models.py
from django.db import models

class Registers(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    mail = models.EmailField()
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Grievance(models.Model):
    GRIEVANCE_CHOICES = [
        ('academic', 'Academic'),
        ('administrative', 'Administrative'),
        ('others', 'Others'),
    ]
    owner=models.ForeignKey(Registers,related_name='user_profile',on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255, blank=True, null=True)  # Optional name field
    department = models.CharField(max_length=255, blank=True, null=True)  # Optional department field
    complaint_title = models.CharField(max_length=255)
    type_of_grievance = models.CharField(max_length=50, choices=GRIEVANCE_CHOICES)
    complaint_description = models.TextField()
    resolution = models.TextField(blank=True, null=True)  # New field for resolution
    assigned_to = models.ForeignKey(Registers, null=True, blank=True, on_delete=models.SET_NULL)  # ForeignKey
    facultyresolution = models.TextField(null=True, blank=True)  # New field for storing resolution

     
    def __str__(self):
        return self.complaint_title

class feedbackforms(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    message=models.CharField(max_length=300)
    resolution = models.TextField(null=True, blank=True)  # New field for storing resolution


    def __str__(self):
        return self.fname


class Appeal(models.Model):
    NATURE_OF_APPEAL_CHOICES = [
        ('administrative', 'Administrative'),
        ('academic', 'Academic'),
        ('student_support', 'Student Support'),
        ('others', 'Others'),
    ]
    owner=models.ForeignKey(Registers,related_name='appeals',on_delete=models.CASCADE,null=True)
    nature_of_appeal = models.CharField(max_length=20, choices=NATURE_OF_APPEAL_CHOICES)
    details_of_appeal = models.TextField()
    proposed_action = models.TextField()
    supporting_documents = models.FileField(upload_to='appeals/documents/', null=True, blank=True)
    signature = models.FileField(upload_to='appeals/signatures/', null=True, blank=True)
    appealresolution = models.TextField(null=True, blank=True)  # New field to store the resolution

    def __str__(self):
        return f"Appeal: {self.nature_of_appeal}"
    

class Event(models.Model):
    event_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.event_type

    def __str__(self):
        return self.event_type