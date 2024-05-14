from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_opening_hours(value):
    if not re.match(r'^[0-1][0-9]:[0-5][0-9] - [0-2][0-9]:[0-5][0-9]$', value):
        raise ValidationError("The format of opening hours must be 'hh:mm - hh:mm'")


class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    code = models.CharField(max_length=16, editable=False, blank=True, null=True)
    opening_morning_hours = models.CharField(
        max_length=20,
        validators=[validate_opening_hours],
        default='09:00 - 14:00',
        blank=False,
        null=False,
    )
    opening_afternoon_hours = models.CharField(
        max_length=20,
        validators=[validate_opening_hours],
        default='14:00 - 19:00',
        blank=False,
        null=False,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            city_code = self.city[:2].upper()
            hotel_code = ''.join(word[:2].upper() for word in self.name.split())
            self.code = f'{city_code}-{hotel_code}'
            self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
