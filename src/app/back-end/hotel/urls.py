from django.urls import path

from .views import HotelAutoComplete

urlpatterns = [
    path('hotels/',
        HotelAutoComplete.as_view(),
        name='hotels',
    ),
]
