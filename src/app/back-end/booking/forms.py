from django import forms
from .models import Booking
from product.models import Product
from django.utils import timezone
from django.db.models import Count


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Booking
        fields = ['products', 'duration', 'date']
        widgets = {
            'duration': forms.Select(choices=Booking.TimeSlots.choices),
        }

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

        total_products_booked = Booking.objects.filter(user=user, date=date).aggregate(
            total=Count('products')
        )['total']

        max_products = user.num_guest

        if total_products_booked + len(products) > max_products:
            raise forms.ValidationError(
                f'You can only reserve a maximum of {max_products} products per day.'
            )

        if date < timezone.now().date():
            raise forms.ValidationError('You cannot book for past dates.')

        max_date = timezone.now().date() + timezone.timedelta(days=7)

        if date > max_date:
            raise forms.ValidationError('You can only book up to one week from today.')

        if products and duration and date:
            if Booking.objects.filter(products__in=products, duration=duration, date=date).exists():
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration '{duration}' on {date}."
                )
            elif (
                duration == 'ALL'
                and Booking.objects.filter(
                    products__in=products, duration__in=['MOR', 'AFT'], date=date
                ).exists()
            ):
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration 'MOR' or 'AFT' on {date}."
                )
            elif (
                duration in ['MOR', 'AFT']
                and Booking.objects.filter(
                    products__in=products, duration='ALL', date=date
                ).exists()
            ):
                raise forms.ValidationError(
                    f"There is already a booking for these products with duration 'ALL' on {date}."
                )
        return cleaned_data
