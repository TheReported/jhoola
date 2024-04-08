from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Client
from .utils import generate_password


class CleanUserData:
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Email already in use.')
        elif email == '':
            raise forms.ValidationError('Email is required for registration.')
        return email

    def clean_first_name(self):
        if first_name := self.cleaned_data.get('first_name'):
            return first_name
        raise forms.ValidationError('First name is required for registration.')

    def clean_last_name(self):
        if last_name := self.cleaned_data.get('last_name'):
            return last_name
        raise forms.ValidationError('Last name is required for registration.')


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class ClientRegistrationForm(forms.ModelForm, CleanUserData):
    password = forms.CharField(
        label='Password',
        validators=[validate_password],
        widget=forms.widgets.HiddenInput(),
    )
    num_guest = forms.IntegerField(
        label='Clients in room',
        validators=[
            MinValueValidator(Client._meta.get_field('num_guest').validators[0].limit_value),
            MaxValueValidator(Client._meta.get_field('num_guest').validators[1].limit_value),
        ],
        initial=3,
    )

    def __init__(self, *args, **kwargs):
        super(ClientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].initial = generate_password()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ClientEditForm(forms.ModelForm, CleanUserData):
    num_guest = forms.IntegerField(
        label='Clients in room',
        validators=[
            MinValueValidator(Client._meta.get_field('num_guest').validators[0].limit_value),
            MaxValueValidator(Client._meta.get_field('num_guest').validators[1].limit_value),
        ],
        initial=3,
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.HiddenInput(),
        }
        required = {
            'password': False,
        }
