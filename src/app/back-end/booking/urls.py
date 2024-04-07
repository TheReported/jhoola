from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('<username>/bookings/', views.booking_list, name='booking_list'),
    path('<username>/bookings/<booking_id>', views.booking_detail, name='booking_detail'),
]
