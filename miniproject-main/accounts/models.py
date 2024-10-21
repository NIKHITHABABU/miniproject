# models.py
from django.db import models

class Registers(models.Model): # Auto-incrementing user ID
    # Add this line if you want an explicit user_id (but Django usually adds an 'id' automatically)
   
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
# Foreign key to Registers (user_id)
    name = models.CharField(max_length=255, blank=True, null=True)  # Optional name field
    department = models.CharField(max_length=255, blank=True, null=True)  # Optional department field
    complaint_title = models.CharField(max_length=255)
    type_of_grievance = models.CharField(max_length=50, choices=GRIEVANCE_CHOICES)
    complaint_description = models.TextField()
    resolution = models.TextField(blank=True, null=True)  # New field for resolution

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

    nature_of_appeal = models.CharField(max_length=20, choices=NATURE_OF_APPEAL_CHOICES)
    details_of_appeal = models.TextField()
    proposed_action = models.TextField()
    supporting_documents = models.FileField(upload_to='appeals/documents/', null=True, blank=True)
    signature = models.FileField(upload_to='appeals/signatures/', null=True, blank=True)

    def __str__(self):
        return f"Appeal: {self.nature_of_appeal}"