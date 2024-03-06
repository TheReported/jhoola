from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, blank=True)
    city = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(
        max_length=12, null=False
    )  # issue: falta validator para comprobar teléfono
    # site_map

    @property
    def code(self):  # issue: crear código a raíz del nombre del hotel
        pass


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(max_length=50, null=False)
    num_guest = models.SmallIntegerField(max_length=2, null=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def create_password(self):  # issue: crear contraseña aleatoria
        pass
