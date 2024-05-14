from django.db import models

from product.models import Product
from users.models import Client
from hotel.models import Hotel


class PaidManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(paid=True)


class Booking(models.Model):
    class TimeSlots(models.TextChoices):
        MORNING = 'MOR', 'Morning'
        AFTERNOON = 'AFT', 'Afternoon'
        ALL_DAY = 'ALL', 'All Day'

        @classmethod
        def get_display_with_hours(cls, slot, morning_hours, afternoon_hours):
            slot_display = dict(cls.choices)[slot]
            if slot == cls.MORNING:
                return f'{slot_display} ({morning_hours})'
            elif slot == cls.AFTERNOON:
                return f'{slot_display} ({afternoon_hours})'
            else:
                return slot_display

    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bookings')
    products = models.ManyToManyField(Product)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=3, choices=TimeSlots.choices)
    date = models.DateField()
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.id}'

    @property
    def get_duration_display(self):
        if self.duration == self.TimeSlots.MORNING:
            return f'Morning ({Hotel.opening_morning_hours})'
        if self.duration == self.TimeSlots.AFTERNOON:
            return f'Afternoon ({Hotel.opening_afternoon_hours})'
        else:
            return 'All Day'
