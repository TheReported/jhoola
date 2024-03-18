from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from product.models import Product
from users.api.permissions import AdminSiteAccess

from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | AdminSiteAccess]
