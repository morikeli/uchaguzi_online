from django import forms
from .models import Polls

class PollingForm(forms.ModelForm):

    class Meta:
        model = Polls
        fields = ['name']