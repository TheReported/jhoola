from rest_framework import serializers

from hotel.api.serializers import HotelSerializer
from users.models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(many=False)

    class Meta:
        model = NewUser
        fields = ['id', 'username', 'hotel', 'email', 'first_name', 'last_name']
