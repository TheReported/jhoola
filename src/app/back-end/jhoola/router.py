from rest_framework import routers

from booking.api.views import BookingViewSet
from hotel.api.views import HotelViewSet
from product.api.views import ProductViewSet
from users.api.views import ClientViewSet

router = routers.DefaultRouter()

app_name = 'router'

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet, basename='hotels')
router.register('clients', ClientViewSet, basename='clients')
router.register('products', ProductViewSet, basename='products')
router.register('bookings', BookingViewSet, basename='bookings')
