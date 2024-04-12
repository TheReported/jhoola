from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking
from users.models import Client
from django.contrib.auth.decorators import login_required
from users.decorators import client_required
from django.template.loader import render_to_string
import weasyprint
from django.http import HttpResponse

from booking.forms import BookingForm


@login_required
@client_required
def booking_list(request, username):
    client = get_object_or_404(Client, user=request.user)
    bookings = Booking.objects.filter(user=client)
    return render(request, 'users/pages/bookings.html', {'bookings': bookings})


@client_required
@login_required
def booking_pdf(request, username, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    html = render_to_string('users/pages/pdf.html', {'booking': booking})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=transaction_{booking_id}.pdf'
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
    return response


@login_required
@client_required
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


@login_required
@client_required
def delete_booking(request, username, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, f'Booking {booking_id} has been succesfully deleted')
    return redirect('booking:booking_list', username=username)
