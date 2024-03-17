from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import NewUser

from .permissions import AdminSiteAccess
from .serializers import NewUserSerializer


class NewUserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAuthenticated, AdminSiteAccess]
