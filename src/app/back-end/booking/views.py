from django.shortcuts import render, redirect

from booking.forms import BookingForm

from django.contrib import messages



from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def booking_view(request, username):
    if request.method == 'POST':
        form = BookingForm(request.user, request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user.client

            product = form.cleaned_data['product']
            duration = form.cleaned_data['duration']

            if product.status == "FR" and not Booking.objects.filter(product=product, duration=duration).exists():
                booking.price = product.price
                booking.save()
                messages.success(request, "You booked the product successfully")
                return redirect('users:manager_users')
            else:
                messages.error(request, "The product is either occupied or not free for the selected duration")
    else:
        form = BookingForm(request.user)
    return render(request, 'users/pages/book.html', {'form': form})