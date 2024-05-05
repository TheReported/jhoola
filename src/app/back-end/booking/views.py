from datetime import datetime

import weasyprint
from celery import shared_task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from booking.forms import BookingFilterForm, BookingForm
from users.decorators import client_required
from users.models import Client

from .models import Booking
from .tasks import booking_created


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
@shared_task
def booking_view(request, username):
    date = request.session.get('date')
    duration = request.session.get('duration')
    formatted_date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    formatted_duration = dict(Booking.TimeSlots.choices)[duration]
    client = get_object_or_404(Client, user=request.user)
    user_bookings = Booking.objects.filter(date=date, user=client)
    total_products = (
        user_bookings.aggregate(total_products=Count('products'))['total_products'] or 0
    )
    max_products = client.num_guest - total_products
    all_date_bookings = Booking.objects.filter(date=date)

    # Inicializar la lista de productos ocupados
    occupied_products = []

    # Filtrar las reservas según la duración seleccionada
    match duration:
        case Booking.TimeSlots.AFTERNOON | Booking.TimeSlots.MORNING:
            # Obtener las reservas de mañana/tarde
            bookings = all_date_bookings.filter(duration=duration)
            # Obtener los productos ocupados de las reservas de mañana/tarde
            occupied_products.extend(
                [product.id for booking in bookings for product in booking.products.all()]
            )
            all_day_bookings = all_date_bookings.filter(duration=Booking.TimeSlots.ALL_DAY)
            for booking in all_day_bookings:
                occupied_products.extend([product.id for product in booking.products.all()])
        case Booking.TimeSlots.ALL_DAY:
            for booking in all_date_bookings:
                occupied_products.extend([product.id for product in booking.products.all()])

    if request.method == 'POST':
        form = BookingForm(user=client, data=request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            products = form.cleaned_data['products']
            if len(products) > max_products:
                messages.error(request, 'You have already reserved all possible hammocks.')
                return redirect('booking:client_book', client)

            total_price = sum(product.price for product in products)
            booking.user = client
            booking.price = total_price
            booking.date = date
            booking.duration = duration
            booking.save()
            form.save_m2m()
            line_items = [
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
            ]
            metadata = {'booking_id': booking.id}
            success_url = request.build_absolute_uri(
                reverse('booking:payment_completed', kwargs={'booking_id': booking.id})
            )
            cancel_url = request.build_absolute_uri(
                reverse('booking:payment_cancelled', kwargs={'booking_id': booking.id})
            )

            task = booking_created.delay(
                success_url,
                cancel_url,
                metadata,
                line_items,
            )
            url = task.get()
            return redirect(url)
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
            'duration': formatted_duration,
            'date': formatted_date,
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
            request.session['date'] = form.cleaned_data['date'].strftime('%Y-%m-%d')
            request.session['duration'] = form.cleaned_data['duration']
            return redirect('booking:client_book', username=username)
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
    else:
        form = BookingFilterForm(user=client)
    return render(request, 'users/pages/filter.html', {'section': 'Book', 'form': form})
