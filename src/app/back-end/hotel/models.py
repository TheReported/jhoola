from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    code = models.CharField(max_length=16, editable=False, blank=True, null=True)
    site_map = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            city_code = self.city[:2].upper()
            hotel_code = ''.join(word[:2].upper() for word in self.name.split())
            self.code = f'{city_code}-{hotel_code}'
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name.capitalize()
