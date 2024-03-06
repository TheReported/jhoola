from django.db import models
from hotel.models import User
from product.models import Product

class Booking(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    duration = models.DurationField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) #issue: comprobar si ManyToMany o ForeignKey
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #issue: comprobar si ManyToMany o ForeignKey
