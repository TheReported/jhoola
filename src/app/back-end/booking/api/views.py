from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from booking.models import Booking
from users.api.permissions import AdminSiteAccess

from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, AdminSiteAccess]
