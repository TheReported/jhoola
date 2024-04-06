from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from hotel.constants import MAX_NUM_GUESTS, MIN_NUM_GUESTS
from hotel.models import Hotel


class Client(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users'
    )
    num_guest = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(MIN_NUM_GUESTS),
            MaxValueValidator(MAX_NUM_GUESTS),
        ],
    )
    telephone = models.CharField(max_length=15)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="clients")

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
