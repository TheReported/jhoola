from django import forms
from .models import Booking
from datetime import timedelta
from product.models import Product

class BookingForm(forms.ModelForm):
    duration = forms.DurationField()
    product = forms.ModelChoiceField(queryset=Product.objects.none(), required=True)

    class Meta:
        model = Booking
        fields = ['product', 'duration']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hotel = user.client.hotel
        self.fields['product'].queryset = Product.objects.filter(hotel=hotel)
        self.fields['duration'].widget = forms.Select(choices=[
            (timedelta(hours=6), '08:00 - 14:00'),
            (timedelta(hours=6), '14:00 - 20:00'),
        ])
