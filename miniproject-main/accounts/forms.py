# forms.py
from django import forms
from .models import Grievance
from .models import Appeal

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['complaint_title', 'type_of_grievance', 'complaint_description']

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['first_name', 'last_name', 'email', 'message']


class AppealForm(forms.ModelForm):
    class Meta:
        model = Appeal
        fields = ['nature_of_appeal', 'details_of_appeal', 'proposed_action', 'supporting_documents', 'signature']