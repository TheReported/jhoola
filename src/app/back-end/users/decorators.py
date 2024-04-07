from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

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
        client = get_object_or_404(Client, user=request.user)
        if client.user.groups.filter(name="HotelManagers").exists():
            return func(request, *args, **kwargs)
        return redirect(
            reverse("users:client_dashboard", kwargs={'username': client.user.username})
        )

    return wrapper
