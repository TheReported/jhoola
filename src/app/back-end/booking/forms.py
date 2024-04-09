from django import forms
from .models import Booking, DURATION_CHOICES

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['product', 'duration']
        widgets = {
            'duration': forms.Select(choices=DURATION_CHOICES),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user 

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user 
        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        duration = cleaned_data.get('duration')
        
        if product and duration:
            if Booking.objects.filter(product=product, duration=duration).exists():
                raise forms.ValidationError(f"There is already a booking for this product with duration '{duration}'.")
            elif duration == 'ALL' and Booking.objects.filter(product=product, duration__in=['MOR', 'AFT']).exists():
                raise forms.ValidationError("There is already a booking for this product with duration 'MOR' or 'AFT'.")
            elif duration in ['MOR', 'AFT'] and Booking.objects.filter(product=product, duration='ALL').exists():
                raise forms.ValidationError("There is already a booking for this product with duration 'ALL'.")
        return cleaned_data
