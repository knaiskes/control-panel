from django import forms
from .models import Relay

class UpdateStateForm(forms.ModelForm):
    class Meta:
        model = Relay
        fields = ('state',)
