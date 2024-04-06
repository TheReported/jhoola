from django import forms

from .models import Client


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'hotel', 'num_guest', 'telephone']


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['user', 'hotel', 'num_guest', 'telephone']
