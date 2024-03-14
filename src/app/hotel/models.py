from django.db import models
import random
import string


class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, blank=True)
    city = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(
        max_length=12, null=False
    )
    code = models.CharField(max_length=16, editable=False)
    # site_map

    def save(self, *args, **kwargs):
        if not self.pk:
            city_code = self.city[:2].upper()
            hotel_code = ''.join(word[:2].upper() for word in self.name.split())
            self.code = f"{city_code}-{hotel_code}"
        super().save(*args, **kwargs)


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.charField(max_length=16, editable=False)
    email = models.EmailField(max_length=50, null=False)
    num_guest = models.SmallIntegerField(max_length=2, null=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            chars = string.ascii_letters + string.digits + string.punctuation
            password_random = ''.join(random.choice(chars) for _ in range(16))
            self.password = make_password(password_random)
        super().save(*args, **kwargs)
    
