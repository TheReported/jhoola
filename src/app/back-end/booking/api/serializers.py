from rest_framework import serializers

from booking.models import Booking
from product.api.serializers import ProductSerializer
from users.api.serializers import ClientSerializer


class BookingSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = Booking
        fields = ['id', 'client', 'product', 'timestamp', 'price', 'duration']
