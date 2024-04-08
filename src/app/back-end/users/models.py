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
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="clients")

    def __str__(self):
        return self.user.username
