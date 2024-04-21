from django import forms
from django.utils import timezone
from product.models import Product

from .models import Booking


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Booking
        fields = ['products', 'duration', 'date']

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

    def clean(self):
        cleaned_data = super().clean()
        products = cleaned_data.get('products')
        duration = cleaned_data.get('duration')
        date = cleaned_data.get('date')
        user = self.user
        max_products = user.num_guest
        actual_date = timezone.now().date()
        max_date = actual_date + timezone.timedelta(days=7)

        if not products:
            raise forms.ValidationError('You have to choose at least one product')

        if len(products) > max_products and (duration == 'ALL' or duration in ['MOR', 'AFT']):
            raise forms.ValidationError(
                f'You can only reserve a maximum of {max_products} products per time slot.'
            )

        if date < actual_date:
            raise forms.ValidationError('You cannot book for past dates.')

        if date > max_date:
            raise forms.ValidationError('You can only book up to one week from today.')

        if products and duration and date:
            if Booking.objects.filter(
                products__in=products, duration=duration, date=date, paid=True
            ).exists():
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration '{duration}' on {date}."
                )
            elif (
                duration == 'ALL'
                and Booking.objects.filter(
                    products__in=products, duration__in=['MOR', 'AFT'], date=date, paid=True
                ).exists()
            ):
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration 'MOR' or 'AFT' on {date}."
                )
            elif (
                duration in ['MOR', 'AFT']
                and Booking.objects.filter(
                    products__in=products, duration='ALL', date=date, paid=True
                ).exists()
            ):
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration 'ALL' on {date}."
                )
        return cleaned_data
