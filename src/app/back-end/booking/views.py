import stripe
import weasyprint
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from booking.forms import BookingFilterForm, BookingForm
from users.decorators import client_required
from users.models import Client

from .models import Booking

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@login_required
@client_required
def booking_list(request, username):
    client = get_object_or_404(Client, user=request.user)
    actual_datetime = timezone.now().date()
    bookings = Booking.objects.filter(user=client, date__gte=actual_datetime, paid=True)
    paginator = Paginator(bookings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'users/pages/bookings.html', {'page_obj': page_obj, 'section': 'My Bookings'}
    )


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
    date = request.session.get("date")
    duration = request.session.get("duration")
    client = get_object_or_404(Client, user=request.user)
    bookings = Booking.objects.filter(date=date, paid=True, duration=duration)
    occupied_products = [product.id for booking in bookings for product in booking.products.all()]
    # Obtener los productos reservados para todo el día
    if duration != Booking.TimeSlots.ALL_DAY:
        all_day_bookings = Booking.objects.filter(
            date=date, paid=True, duration=Booking.TimeSlots.ALL_DAY
        )
        all_day_products = [
            product.id for booking in all_day_bookings for product in booking.products.all()
        ]

        # Verificar y agregar los productos reservados para todo el día si no están ya en la lista
        for product_id in all_day_products:
            if product_id not in occupied_products:
                occupied_products.append(product_id)

    if request.method == 'POST':
        form = BookingForm(user=client, data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            products = form.cleaned_data['products']
            total_price = sum(product.price for product in products)

            booking.user = client
            booking.price = total_price
            booking.date = date
            booking.duration = duration
            booking.save()
            form.save_m2m()
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'product_data': {
                                'name': 'Booking',
                            },
                            'unit_amount': int(total_price * 100),
                        },
                        'quantity': 1,
                    }
                ],
                mode='payment',
                metadata={'booking_id': booking.id},
                success_url=request.build_absolute_uri(
                    reverse('booking:payment_completed', kwargs={'booking_id': booking.id})
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('booking:payment_cancelled', kwargs={'booking_id': booking.id})
                ),
            )
            return redirect(session.url)
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)

    else:
        form = BookingForm(user=client)
    return render(
        request,
        'users/pages/book.html',
        {
            'form': form,
            'section': 'Book',
            'occupied_products': occupied_products,
            'duration': duration,
            'date': date,
        },
    )


@client_required
@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.paid = True
    booking.save()
    messages.success(request, 'Your hammocks have been properly booked')
    return redirect('booking:booking_list', booking.user)


@client_required
@login_required
def payment_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.error(request, 'There has been an error with your booking')
    return redirect('booking:booking_list', booking.user)


@login_required
@client_required
def delete_booking(request, username, booking_id):
    client = get_object_or_404(Client, user=request.user)
    booking = get_object_or_404(Booking, id=booking_id, user=client)
    booking.delete()
    messages.success(request, f'Booking {booking_id} has been succesfully deleted')
    return redirect('booking:booking_list', username=username)


@login_required
@client_required
def filter_view(request, username):
    client = get_object_or_404(Client, user=request.user)
    if request.method == 'POST':
        form = BookingFilterForm(user=client, data=request.POST)
        if form.is_valid():
            request.session["date"] = form.cleaned_data["date"].strftime("%Y-%m-%d")
            request.session["duration"] = form.cleaned_data["duration"]
            return redirect("booking:client_book", username=username)
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
    else:
        form = BookingFilterForm(user=client)
    return render(request, "users/pages/filter.html", {"section": "Book", "form": form})
