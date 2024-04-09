from django import forms
from .models import Booking
from product.models import Product

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  

    class Meta:
        model = Booking
        fields = ['product', 'duration', 'date']  
        widgets = {
            'duration': forms.Select(choices=Booking.TimeSlots.choices),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user 
        self.fields['product'].queryset = Product.objects.filter(hotel=self.user.hotel)

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
        date = cleaned_data.get('date')

        if product and duration and date:
            if Booking.objects.filter(product=product, duration=duration, date=date).exists():
                raise forms.ValidationError(f"There is already a booking for this product with duration '{duration}' on {date}.")
            elif duration == 'ALL' and Booking.objects.filter(product=product, duration__in=['MOR', 'AFT'], date=date).exists():
                raise forms.ValidationError(f"There is already a booking for this product with duration 'MOR' or 'AFT' on {date}.")
            elif duration in ['MOR', 'AFT'] and Booking.objects.filter(product=product, duration='ALL', date=date).exists():
                raise forms.ValidationError(f"There is already a booking for this product with duration 'ALL' on {date}.")
        return cleaned_data
