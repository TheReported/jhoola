from django.db import models
from product.models import Product
from users.models import Client


class Booking(models.Model):
    class TimeSlots(models.TextChoices):
        MORNING = 'MOR', 'Morning'
        AFTERNOON = 'AFT', 'Afternoon'
        ALL_DAY = 'ALL', 'All Day'

    user = models.ForeignKey(Client, on_delete=models.CASCADE)
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
