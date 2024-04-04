from django import forms
from .models import Hotel
from dal import autocomplete


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name',)
        widgets = {
            'name': autocomplete.ModelSelect2(url='hotel-autocomplete'),
        }
