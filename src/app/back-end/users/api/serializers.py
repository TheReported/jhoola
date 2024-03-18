from django.contrib.auth.models import User
from rest_framework import serializers

from hotel.api.serializers import HotelSerializer
from users.models import Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    hotel = HotelSerializer(many=False)

    class Meta:
        model = Client
        fields = ['id', 'user', 'hotel', 'num_guest']
