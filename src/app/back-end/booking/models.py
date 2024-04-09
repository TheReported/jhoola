from django.db import models

from product.models import Product
from users.models import Client

DURATION_CHOICES = [
        ('MOR', 'Morning'),
        ('AFT', 'Afternoon'),
        ('ALL', 'All Day'),
    ]

class Booking(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=3, choices=DURATION_CHOICES)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self) -> str:
        return f'{self.user} -> {self.product} {self.duration}'
