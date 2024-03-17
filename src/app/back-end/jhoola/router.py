from rest_framework import routers

from booking.api.views import BookingViewSet
from hotel.api.views import HotelViewSet
from product.api.views import ProductViewSet
from users.api.views import NewUserViewSet

router = routers.DefaultRouter()

app_name = 'router'

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet, basename='hotels')
router.register('users', NewUserViewSet, basename='users')
router.register('products', ProductViewSet, basename='products')
router.register('bookings', BookingViewSet, basename='bookings')
