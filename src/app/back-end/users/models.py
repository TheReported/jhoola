from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from hotel.models import Hotel

# Minimum and maximun number of guests per room
MIN_NUM_GUESTS = 1
MAX_NUM_GUESTS = 10


class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client'
    )
    num_guest = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_NUM_GUESTS),
            MaxValueValidator(MAX_NUM_GUESTS),
        ],
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='clients')

    def save(self, *args, **kwargs):
        # password = generate_password()
        # subject = 'Jhoola'
        # message = f'You have a new user in hotel {str(self.hotel)} and your password is {password}'
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [self.email]
        # send_mail(subject, message, from_email, to_email, fail_silently=False)
        # self.password = make_password(password)
        super().save(self, *args, **kwargs)

    def __str__(self):
        return self.user.username
