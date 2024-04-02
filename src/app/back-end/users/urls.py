from django.urls import include, path

from . import views

app_name = "users"
urlpatterns = [
    path('bookings/', views.client_dashboard, name='client_dashboard'),
    path(
        'manager/', views.manager_dashboard, name='manager_dashboard'
    ),  # TODO: Meter slug cuando mande formulario del hotel
]
