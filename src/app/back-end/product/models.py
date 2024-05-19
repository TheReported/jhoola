from django.db import models

from hotel.models import Hotel


class FreeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.FREE)


class OccupiedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.OCCUPIED)


class Product(models.Model):
    class Status(models.TextChoices):
        FREE = 'FR', 'Free'
        OCCUPIED = 'OC', 'Occupied'

    name = models.CharField(max_length=30, default='Hammock')
    price = models.DecimalField(max_digits=4, decimal_places=2, null=False, default=2.5)
    avatar = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=2, choices=Status.choices, default='FR')
    hotel = models.ForeignKey(Hotel, related_name='products', on_delete=models.CASCADE)
    hotel_product_id = models.PositiveIntegerField(editable=False, blank=True, null=True)

    objects = models.Manager()
    free = FreeManager()
    occupied = OccupiedManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            last_product = (
                Product.objects.filter(hotel=self.hotel).order_by('hotel_product_id').last()
            )
            if last_product:
                self.hotel_product_id = last_product.hotel_product_id + 1
            else:
                self.hotel_product_id = 1
        super().save(*args, **kwargs)
