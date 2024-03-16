from django.db import models

from product.models import Product
from users.models import NewUser


class Booking(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DurationField()

    class Meta:
        ordering = ['-timestamp']
