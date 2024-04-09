from django.shortcuts import render, redirect

from booking.forms import BookingForm
from .models import Client


from django.shortcuts import render, redirect
from .forms import BookingForm

def booking_view(request, username):
    client = Client.objects.get(user=request.user) 
    if request.method == 'POST':
        form = BookingForm(user=client, data=request.POST)  
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = client  
            booking.price = 0 
            booking.save()
            return redirect('users:manager_users')

    else:
        form = BookingForm(user=client)  
    return render(request, 'users/pages/book.html', {'form': form})
