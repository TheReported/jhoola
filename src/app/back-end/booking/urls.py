from django.urls import path

from . import views

app_name = 'booking'
urlpatterns = [
    path('<str:username>/book/', views.booking_view, name='client_book'),
    path('<str:username>/bookings/', views.booking_list, name='booking_list'),
    path('<str:username>/bookings/<booking_id>/pdf/', views.booking_pdf, name='booking_pdf'),
    path('<str:username>/bookings/<booking_id>/delete', views.delete_booking, name='delete_booking'),

]
