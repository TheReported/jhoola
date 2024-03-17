from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from hotel.constants import MAX_NUM_GUESTS, MIN_NUM_GUESTS
from hotel.models import Hotel
from users.utils import generate_password


class NewUser(User):

    num_guest = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_NUM_GUESTS),
            MaxValueValidator(MAX_NUM_GUESTS),
        ],
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Send email to User with his password
        password = generate_password()
        self.password = make_password(password)
        super().save(self, *args, **kwargs)
