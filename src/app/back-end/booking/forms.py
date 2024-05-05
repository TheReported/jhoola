from django import forms
from django.utils import timezone

from product.models import Product

from .models import Booking


class BookingFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    duration = forms.ChoiceField(choices=Booking.TimeSlots.choices)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['duration'].initial = Booking.TimeSlots.ALL_DAY

    def clean_date(self):
        date = self.cleaned_data.get("date")
        actual_date = timezone.now().date()
        max_date = actual_date + timezone.timedelta(days=7)

        if actual_date <= date > max_date:
            raise forms.ValidationError('You can only book up to one week from today.')
        if date < actual_date:
            raise forms.ValidationError('You cannot book for past dates.')
        return date

    # def clean_duration(self):
    #     duration = self.cleaned_data.get("duration")
    #     date = self.cleaned_data.get("date")
    #     bookings = Booking.objects.filter(date=date, duration=duration, user=self.user)
    #     if bookings.exists():
    #         raise forms.ValidationError('You can only book one time for duration')
    #     return duration

    # IDEA A DESARROLLAR: Controlar en la vista la actualización de los productos máximos tal que así
    # def clean(self):
    #     date = request.session.get("date")
    #     duration = request.session.get("duration")
    #     bookings = Booking.objects.filter(user=self.user, date=date, duration=duration)
    #     total_products = bookings.aggregate(total_products=Count('products'))['total_products'] or 0
    #     max_products = self.user.num_guest - total_products


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
