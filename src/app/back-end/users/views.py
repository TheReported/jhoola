from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from booking.forms import BookingFilterForm, BookingForm
from booking.models import Booking
from product.forms import ProductCreationForm, ProductEditForm
from product.models import Product

from .decorators import manager_required
from .forms import ClientEditForm, ClientRegistrationForm, LoginForm, SearchForm
from .models import Client, Hotel


def user_login(request):
    selected_hotel = request.session.get('hotel_session_name')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                hotel = get_object_or_404(Hotel, name=selected_hotel)
                client = get_object_or_404(Client, user=user)
                if client.hotel == hotel:
                    login(request, user)
                    if user.groups.filter(name='HotelManagers').exists():
                        return redirect('users:manager_dashboard')
                    return redirect('booking:booking_list', username=user.username)
                messages.error(request, "You are accessing a hotel where you aren't authenticated.")
            else:
                messages.error(request, 'The credentials entered are incorrect. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
@manager_required
def manager_dashboard(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    clients = hotel.clients.count()
    products = hotel.products.count()
    bookings = Booking.objects.filter(user__hotel=hotel, paid=True)
    total_money = 0
    for booking in bookings:
        total_money += booking.price

    return render(
        request,
        'managers/dashboard-manager.html',
        {
            'num_products': products,
            'num_clients': clients,
            'num_bookings': bookings.count(),
            'total_money': total_money,
        },
    )


@login_required
@manager_required
def users_add_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    hotel_abbreviation = ''.join(letter[0] for letter in hotel.name.split()).upper()
    city_abbreviation = ''.join(letter[0] for letter in hotel.city.split()).upper()
    if request.method == 'POST':
        user_form = ClientRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(cd['password'])
            new_user.save()
            Client.objects.create(user=new_user, hotel=hotel, num_guest=cd['num_guest'])
            subject = 'Welcome to Jhoola!'
            message = f"""
We are delighted to have you with us, {new_user.get_full_name()}! We hope your stay at our hotel will
be absolutely exceptional.

Username: {new_user.username}
Hotel name: {hotel}
Password : {cd['password']}

We hope you enjoy all the amenities and services we offer during your visit!
Please remember to keep your password secure at all times to ensure the safety of your account and personal information.
"""
            from_email = settings.EMAIL_HOST_USER
            to_email = [cd['email']]
            send_mail(subject, message, from_email, to_email, fail_silently=False)

            messages.success(request, 'A new client has been successfully created.')
            return redirect('users:manager_users')
        messages.error(request, "New client couldn't be created")
    else:
        user_form = ClientRegistrationForm(
            initial={
                'username': f'{hotel_abbreviation}{city_abbreviation}-{hotel.clients.last().id:04d}'
            }
        )
    return render(
        request,
        'managers/pages/users_add.html',
        {'user_form': user_form},
    )


@login_required
@manager_required
def users_edit_manager_view(request, username):
    client = get_object_or_404(Client, user__username=username)
    if request.method == 'POST':
        user_edit_form = ClientEditForm(instance=client.user, data=request.POST)
        if user_edit_form.is_valid():
            cd = user_edit_form.cleaned_data
            user = user_edit_form.save(commit=False)
            client.num_guest = cd['num_guest']
            user.save()
            client.save()
            messages.success(request, 'A new client has been successfully edited.')
            return redirect('users:manager_users')
        messages.error(request, "New client couldn't be edited")
    else:
        user_edit_form = ClientEditForm(instance=client.user)
    return render(
        request,
        'managers/pages/users_edit.html',
        {
            'user_edit_form': user_edit_form,
            'client': client,
        },
    )


@login_required
@manager_required
@require_POST
def users_delete_manager_view(request, username):
    client = get_object_or_404(Client, user__username=username)
    client.user.delete()
    client.delete()
    return redirect('users:manager_users')


@login_required
@manager_required
def users_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    clients = hotel.clients.exclude(user__groups__name='HotelManagers')
    paginator = Paginator(clients, 4)
    page = request.GET.get('page')

    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    return render(
        request,
        'managers/pages/users.html',
        {'clients': clients},
    )


@login_required
@manager_required
def products_delete_manager_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('users:manager_products')


@login_required
@manager_required
def products_edit_manager_view(request, product_id):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    product = hotel.products.get(id=product_id)
    if request.method == 'POST':
        product_edit_form = ProductEditForm(instance=product, data=request.POST)
        if product_edit_form.is_valid():
            product.save()
            messages.success(request, 'A new product has been successfully edited.')
            return redirect('users:manager_products')
        messages.error(request, "New product couldn't be edited")
    else:
        product_edit_form = ProductEditForm(instance=product)
    return render(
        request,
        'managers/pages/products_edit.html',
        {
            'product_edit_form': product_edit_form,
            'product': product,
        },
    )


@login_required
@manager_required
def products_add_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    if request.method == 'POST':
        product_add_form = ProductCreationForm(request.POST)
        if product_add_form.is_valid():
            product = product_add_form.save(commit=False)
            product.hotel = hotel
            product.save()
            messages.success(request, 'A new product has been successfully created.')
            return redirect('users:manager_products')
        messages.error(request, "New product couldn't be created")
    else:
        product_add_form = ProductCreationForm()
    return render(
        request,
        'managers/pages/products_add.html',
        {
            'product_add_form': product_add_form,
        },
    )


@login_required
@manager_required
def products_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    products = hotel.products.all()
    paginator = Paginator(products, 4)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'managers/pages/products.html', {'products': products})


@login_required
@manager_required
def bookings_edit_manager_view(request, booking_id):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    booking = get_object_or_404(Booking, id=booking_id, user__hotel=hotel, paid=True)
    if request.method == 'POST':
        booking_edit_form = BookingForm(user=booking.user, data=request.POST)
        booking_edit_filter_form = BookingFilterForm(
            user=booking.user, instance=booking, data=request.POST
        )
        if booking_edit_form.is_valid():
            booking.save()
            messages.success(request, 'A new booking has been successfully edited.')
            return redirect('users:manager_bookings')
        messages.error(request, "New booking couldn't be edited")
    else:
        booking_edit_form = BookingForm(user=booking.user, instance=booking)
        booking_edit_filter_form = BookingFilterForm(
            user=booking.user, data={"date": booking.date, "duration": booking.duration}
        )
    return render(
        request,
        'managers/pages/bookings_edit.html',
        {
            'booking_edit_form': booking_edit_form,
            'booking_edit_filter_form': booking_edit_filter_form,
            'booking': booking,
        },
    )


@login_required
@manager_required
def bookings_delete_manager_view(request, booking_id):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    booking = get_object_or_404(Booking, id=booking_id, user__hotel=hotel, paid=True)
    booking.delete()
    return redirect('users:manager_bookings')


@login_required
@manager_required
def bookings_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    bookings = Booking.objects.filter(user__hotel=hotel, paid=True)
    paginator = Paginator(bookings, 4)
    page = request.GET.get('page')

    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)

    return render(request, 'managers/pages/bookings.html', {'bookings': bookings})


@login_required
@manager_required
def search_manager_view(request):
    form = SearchForm(request.GET)
    clients = []
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)

    if form.is_valid():
        query = form.cleaned_data['query']
        clients = (
            hotel.clients.filter(
                Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)
                | Q(user__username__icontains=query)
                | Q(user__email__icontains=query)
            )
            .distinct()
            .exclude(user__groups__name='HotelManagers')
        )

    return render(
        request,
        'managers/pages/search_list.html',
        {
            'form': form,
            'clients': clients,
        },
    )
