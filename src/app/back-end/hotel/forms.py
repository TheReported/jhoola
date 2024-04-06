from django import forms


class HotelForm(forms.Form):
    hotel_selector = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'hotel-input', 'placeholder': 'Choose your hotel'}),
    )
