from rest_framework import viewsets

from hotel.models import Hotel

from .permissions import PublicGetOnly
from .serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    http_method_names = ['get']
    permission_classes = [PublicGetOnly]
