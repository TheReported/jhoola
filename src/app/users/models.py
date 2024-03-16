import random
import string

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from hotel.constants import MAX_NUM_GUESTS, MIN_NUM_GUESTS
from hotel.models import Hotel


class NewUser(User):
    num_guest = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_NUM_GUESTS),
            MaxValueValidator(MAX_NUM_GUESTS),
        ],
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            chars = (char for char in string.printable if char not in string.whitespace)
            self.password = ''.join(random.choice(chars) for _ in range(10))
        super().save(*args, **kwargs)
