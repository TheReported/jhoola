from rest_framework import serializers

from booking.models import Booking
from product.api.serializers import ProductSerializer
from users.api.serializers import ClientSerializer


class BookingSerializer(serializers.ModelSerializer):
    user = ClientSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'products', 'date', 'price', 'duration']
