from rest_framework import serializers

from booking.models import Booking
from product.api.serializers import ProductSerializer
from users.api.serializers import NewUserSerializer


class BookingSerializer(serializers.ModelSerializer):
    user = NewUserSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'product', 'timestamp', 'price', 'duration']
