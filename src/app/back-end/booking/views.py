from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from users.models import Client
from django.contrib.auth.decorators import login_required
from users.decorators import client_required


from booking.forms import BookingForm


@login_required
@client_required
def booking_list(request, username):
    client = get_object_or_404(Client, user=request.user)
    bookings = Booking.objects.filter(user=client)
    return render(request, 'users/pages/bookings.html', {'bookings': bookings})


def booking_detail(request, username, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'users/pages/booking_detail.html', {'booking': booking})


def booking_view(request, username):
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = BookingForm(client, request.POST)
        if form.is_valid():
            form.instance.price = 0
            form.save()
            return redirect('users:manager_users')

    else:
        form = BookingForm(request.user)
    return render(request, 'users/pages/book.html', {'form': form})
