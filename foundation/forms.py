from django import forms
from .models import Donation, Volunteer

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'purpose', 'donor_name', 'phone_number']

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email'] 