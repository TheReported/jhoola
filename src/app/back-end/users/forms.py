from django import forms

from .models import Client


class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'hotel', 'num_guest']


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'hotel', 'num_guest']
