from rest_framework import serializers

from hotel.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'slug', 'city', 'country', 'code', 'opening_morning_hours', 'opening_afternoon_hours']
