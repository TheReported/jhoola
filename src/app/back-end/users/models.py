from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from hotel.models import Hotel

# Minimum and maximun number of guests per room
MIN_NUM_GUESTS = 1
MAX_NUM_GUESTS = 10


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num_guest = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_NUM_GUESTS),
            MaxValueValidator(MAX_NUM_GUESTS),
        ],
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='clients')
    hotel_client_id = models.PositiveIntegerField(editable=False, blank=True, null=True)

    @property
    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            last_client = (
                Client.objects.filter(hotel=self.hotel).order_by('hotel_client_id').last()
            )
            if last_client:
                self.hotel_client_id = last_client.hotel_client_id + 1
            else:
                self.hotel_client_id = 1
        super().save(*args, **kwargs)
