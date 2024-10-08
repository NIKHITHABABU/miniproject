# forms.py
from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['complaint_title', 'type_of_grievance', 'complaint_description']

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['first_name', 'last_name', 'email', 'message']
