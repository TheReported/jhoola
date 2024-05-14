from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Client
from .utils import generate_password


class CleanUserData:
    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError('Email is required for registration.')
        elif User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Email already in use.')
        return email

    def clean_first_name(self):
        if first_name := self.cleaned_data.get('first_name'):
            return first_name
        raise forms.ValidationError('First name is required for registration.')

    def clean_last_name(self):
        if last_name := self.cleaned_data.get('last_name'):
            return last_name
        raise forms.ValidationError('Last name is required for registration.')

    def clean_num_guest(self):
        if num_guest := self.cleaned_data.get('num_guest'):
            return num_guest
        raise forms.ValidationError('Clients in room is required for registration.')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username', widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class ClientRegistrationForm(forms.ModelForm, CleanUserData):
    def __init__(self, *args, **kwargs):
        super(ClientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].initial = generate_password()

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
        initial=1,
        min_value=1,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ClientEditForm(forms.ModelForm, CleanUserData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            initial_num_guest = self.instance.client.num_guest
            self.fields['num_guest'].initial = initial_num_guest

    num_guest = forms.IntegerField(
        label='Clients in room',
        required=False,
        validators=[
            MinValueValidator(Client._meta.get_field('num_guest').validators[0].limit_value),
            MaxValueValidator(Client._meta.get_field('num_guest').validators[1].limit_value),
        ],
        min_value=1,
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


class SearchForm(forms.Form):
    query = forms.CharField()


class SupportForm(forms.Form):
    subject = forms.CharField(
        max_length=100, label='subject', widget=forms.TextInput(attrs={'placeholder': 'Subject'})
    )
    email = forms.CharField(
        max_length=200, label='email', widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    name = forms.CharField(
        max_length=100, label='name', widget=forms.TextInput(attrs={'placeholder': 'Name'})
    )
    message = forms.CharField(
        max_length=300,
        label='message',
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': "4", 'cols': "30"}),
    )
