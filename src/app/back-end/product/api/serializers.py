from rest_framework import serializers

from hotel.api.serializers import HotelSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(many=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'status', 'avatar', 'hotel']
