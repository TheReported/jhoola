from django import forms

from .models import Booking


class BookingCreationForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'product', 'price', 'duration']


class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'product', 'price', 'duration']
