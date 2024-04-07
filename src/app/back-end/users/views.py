from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from booking.models import Booking
from product.models import Product

from .decorators import client_required, manager_required
from .forms import ClientEditForm, ClientRegistrationForm, LoginForm
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
                    return redirect('users:client_dashboard', username=user.username)
                messages.error(
                    request, 'You are accessing a hotel where you aren\'t authenticated.'
                )
            else:
                messages.error(request, 'The credentials entered are incorrect. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
@client_required
def client_dashboard(request, username):
    client = get_object_or_404(Client, user=request.user)
    return render(request, 'users/dashboard.html', {'client': client})


@login_required
@manager_required
def manager_dashboard(request):
    client = get_object_or_404(Client, user=request.user)
    clients = Client.objects.filter(hotel=client.hotel).count()
    products = Product.objects.filter(hotel=client.hotel).count()
    bookings = Booking.objects.filter(user__hotel=client.hotel)
    total_money = 0
    for booking in bookings:
        total_money += booking.price

    return render(
        request,
        'managers/dashboard-manager.html',
        {
            'client': client,
            'num_products': products,
            'num_clients': clients,
            'num_bookings': bookings.count(),
            'total_money': total_money,
        },
    )


@login_required
@manager_required
def users_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    hotel_abbreviation = ''.join(letter[0] for letter in hotel.name.split()).upper()
    city_abbreviation = ''.join(letter[0] for letter in hotel.city.split()).upper()
    clients = Client.objects.filter(hotel=hotel)
    if request.method == 'POST':
        user_form = ClientRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Client.objects.create(
                user=new_user, hotel=hotel, num_guest=user_form.cleaned_data['num_guest']
            )
            messages.success(request, 'A new client has been successfully created.')
        messages.error(request, 'New client couldn\'t be created')
    else:

        user_form = ClientRegistrationForm(
            initial={'username': f'{hotel_abbreviation}{city_abbreviation}-{clients.count():04d}'}
        )
        user_edit_form = ClientEditForm()
    return render(
        request,
        'managers/pages/users.html',
        {'user_form': user_form, 'clients': clients, 'user_edit_form': user_edit_form},
    )


@login_required
@manager_required
def products_manager_view(request):
    return render(request, 'managers/pages/products.html', {})


@login_required
@manager_required
def bookings_manager_view(request):
    return render(request, 'managers/pages/bookings.html', {})
