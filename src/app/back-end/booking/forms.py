from django import forms
from django.utils import timezone

from product.models import Product

from .models import Booking
from hotel.models import Hotel  


class BookingFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    duration = forms.ChoiceField()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['duration'].choices = self.get_duration_choices(self.user.hotel)
        self.fields['duration'].initial = Booking.TimeSlots.ALL_DAY

    def clean_date(self):
        date = self.cleaned_data.get('date')
        actual_date = timezone.now().date()
        max_date = actual_date + timezone.timedelta(days=7)

        if actual_date <= date > max_date:
            raise forms.ValidationError('You can only reserve up to one week from today.')
        if date < actual_date:
            raise forms.ValidationError('You cannot reserve for past dates.')
        return date

    def get_duration_choices(self,hotel):
        hotel = Hotel.objects.get(id=hotel.id)
        morning_hours = hotel.opening_morning_hours
        afternoon_hours = hotel.opening_afternoon_hours

        duration_choices = [
            (choice[0], Booking.TimeSlots.get_display_with_hours(choice[0], morning_hours, afternoon_hours)) 
            for choice in Booking.TimeSlots.choices
        ]
        return duration_choices


class BookingForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Booking
        fields = ['products']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['products'].queryset = Product.objects.filter(hotel=self.user.hotel)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance

    def clean_products(self):
        products = self.cleaned_data.get('products')
        user = self.user
        max_products = user.num_guest

        if not products:
            raise forms.ValidationError('You have to choose at least one product')

        if len(products) > max_products:
            raise forms.ValidationError(
                f'You can only reserve a maximum of {max_products} products per time slot.'
            )

        return products
