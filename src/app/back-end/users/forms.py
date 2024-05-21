from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Client
from .utils import generate_password


class CleanUserData:
    def clean_email(self):
        email = self.cleaned_data['email']
        hotel = self.cleaned_data['hotel']
        if email == '':
            raise forms.ValidationError('Email is required for registration.')
        elif Client.objects.filter(email=email, hotel=hotel).exclude(id=self.instance.id).exists():
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


class ClientRegistrationForm(forms.Form):

    username = forms.CharField(label='Username')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email')
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
    hotel = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(ClientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].initial = generate_password()

    def clean_email(self):
        email = self.cleaned_data['email']
        hotel = self.data['hotel']
        if email == '':
            raise forms.ValidationError('Email is required for registration.')
        try:
            client = Client.objects.get(user__email=email, hotel__name=hotel)
            if client:
                raise forms.ValidationError('Email already in use.')
        except Client.DoesNotExist:
            return email
        return email

    def clean_first_name(self):
        if first_name := self.cleaned_data.get('first_name'):
            return first_name
        raise forms.ValidationError('First name is required for registration.')

    def clean_last_name(self):
        if last_name := self.cleaned_data.get('last_name'):
            return last_name
        raise forms.ValidationError('Last name is required for registration.')

    def clean_password(self):
        if password := self.data.get('password'):
            return password


class ClientEditForm(forms.ModelForm, CleanUserData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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

    hotel = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        hotel = self.data['hotel']
        try:
            user = Client.objects.get(user__username=username)
        except Client.DoesNotExist:
            raise forms.ValidationError("The client username doesn't exist.")
        if email == '':
            raise forms.ValidationError('Email is required for registration.')
        try:
            client = Client.objects.get(user__email=email, hotel__name=hotel)
            if client and user.user.email != email:
                raise forms.ValidationError('Email already in use.')
            return email
        except Client.DoesNotExist:
            return email

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
