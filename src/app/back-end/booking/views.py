from django.shortcuts import render, redirect

from booking.forms import BookingForm
from .models import Client


from django.shortcuts import render, redirect
from .forms import BookingForm

def booking_view(request, username):
    client = Client.objects.get(user = request.user)
    if request.method == 'POST':
        form = BookingForm(client, request.POST)
        if form.is_valid():
            form.instance.price = 0
            form.save()
            return redirect('users:manager_users')

    else:
        form = BookingForm(request.user)
    return render(request, 'users/pages/book.html', {'form': form})