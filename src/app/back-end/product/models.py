from django.db import models

from hotel.models import Hotel


class Product(models.Model):
    class Status(models.TextChoices):
        FREE = 'FR', 'Free'
        OCCUPIED = 'OC', 'Occupied'

    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    avatar = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=Status.choices, default='FR')
    hotel = models.ForeignKey(Hotel, related_name='products', on_delete=models.CASCADE)
