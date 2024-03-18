from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from users.models import Client

from .permissions import AdminSiteAccess
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser | AdminSiteAccess]

    def get_queryset(self):

        if self.request.user.is_staff:
            return Client.objects.all()
        client = Client.objects.get(user=self.request.user)
        return Client.objects.filter(hotel=client.hotel)
