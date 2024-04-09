from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('<username>/bookings/', views.booking_list, name='booking_list'),
    path('<username>/bookings/<booking_id>/pdf/', views.booking_pdf, name='booking_pdf'),
]
