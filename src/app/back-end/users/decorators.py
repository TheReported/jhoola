from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from hotel.models import Hotel

from .models import Client


def client_required(func):
    def wrapper(request, *args, **kwargs):
        client = get_object_or_404(Client, user=request.user)
        if not client.user.groups.filter(name="HotelManagers").exists():
            return func(request, *args, **kwargs)
        return redirect("users:manager_dashboard")

    return wrapper


def manager_required(func):
    def wrapper(request, *args, **kwargs):
        selected_hotel = request.session.get('hotel_session_name')
        hotel = Hotel.objects.get(name=selected_hotel)
        if not request.user.is_authenticated:
            return redirect("users_login")
        client = get_object_or_404(Client, user=request.user, hotel=hotel)
        if client.user.groups.filter(name="HotelManagers").exists():
            return func(request, *args, **kwargs)
        return redirect(reverse("booking:booking_list", kwargs={'username': client.user.username}))

    return wrapper
