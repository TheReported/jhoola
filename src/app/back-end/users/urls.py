from django.urls import path

from . import views

from booking.views import booking_view 

app_name = 'users'
urlpatterns = [
    path('manager/bookings/', views.bookings_manager_view, name='manager_bookings'),
    path('manager/products/', views.products_manager_view, name='manager_products'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/users/', views.users_manager_view, name='manager_users'),
    path('<username>/bookings/', views.client_dashboard, name='client_dashboard'),
    path('<username>/book/', booking_view, name='client_book'),

]
