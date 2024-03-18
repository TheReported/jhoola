from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from hotel.models import Hotel
from users.api.permissions import AdminSiteAccess

from .serializers import HotelSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser | AdminSiteAccess]
