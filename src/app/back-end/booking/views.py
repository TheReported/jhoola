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
            products = form.cleaned_data['products']
            total_price = sum(product.price for product in products)

            booking.user = client
            booking.price = total_price
            booking.save()
            form.save_m2m()  
            return redirect('users:manager_users')
    else:
        form = BookingForm(user=client)
    return render(request, 'users/pages/book.html', {'form': form})
