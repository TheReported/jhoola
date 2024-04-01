from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from booking.models import Booking
from users.api.permissions import AdminSiteAccess
from users.models import Client

from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):

    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser | AdminSiteAccess]

    def get_queryset(self):
        bookings = Booking.objects.all()
        if self.request.user.is_staff:
            return bookings
        client = Client.objects.get(user=self.request.user)
        return bookings.filter(user__hotel=client.hotel)
