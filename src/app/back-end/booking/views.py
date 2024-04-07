from django.shortcuts import render, get_object_or_404
from .models import Booking
from users.models import Client
from product.models import Product
from django.contrib.auth.decorators import login_required
from users.decorators import client_required

@login_required
@client_required
def booking_list(request, username):
    client = get_object_or_404(Client, user=request.user)
    bookings = Booking.objects.filter(user=client)
    return render(request, 'users/pages/bookings.html', {'bookings': bookings})

def booking_detail(request, username, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'users/pages/booking_detail.html', {'booking': booking})


