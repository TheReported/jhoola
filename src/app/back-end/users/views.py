from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from booking.models import Booking
from product.forms import ProductCreationForm, ProductEditForm
from product.models import Product

from .decorators import manager_required
from .forms import ClientEditForm, ClientRegistrationForm, LoginForm, SearchForm
from .models import Client, Hotel
from .tasks import user_created
from django.contrib.auth.models import Group


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
    hotel_manager_group = Group.objects.get(name='HotelManagers')
    clients = hotel.clients.exclude(user__groups=hotel_manager_group).count()
    products = hotel.products.count()
    bookings = Booking.objects.filter(user__hotel=hotel, paid=True)
    total_money = 0
    for booking in bookings:
        total_money += booking.price

    return render(
        request,
        'managers/dashboard-manager.html',
        {
            'hotel': selected_hotel,
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
            user_created.delay(cd, hotel.name)
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
    messages.success(request, f'Client {username} has been succesfully deleted')
    return redirect('users:manager_users')


@login_required
@manager_required
def users_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    clients = hotel.clients.exclude(user__groups__name='HotelManagers')
    paginator = Paginator(clients, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'managers/pages/users.html',
        {'page_obj': page_obj},
    )


@login_required
@manager_required
def products_delete_manager_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, f'Product {product_id} has been succesfully deleted')
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
            messages.success(request, 'Product has been successfully edited.')
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
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'managers/pages/products.html', {'page_obj': page_obj})


@login_required
@manager_required
def bookings_delete_manager_view(request, booking_id):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    booking = get_object_or_404(Booking, id=booking_id, user__hotel=hotel, paid=True)
    booking.delete()
    messages.success(request, f'Reservation {booking_id} has been succesfully deleted')
    return redirect('users:manager_bookings')


@login_required
@manager_required
def bookings_manager_view(request):
    selected_hotel = request.session.get('hotel_session_name')
    hotel = Hotel.objects.get(name=selected_hotel)
    bookings = Booking.objects.filter(user__hotel=hotel, paid=True)
    paginator = Paginator(bookings, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'managers/pages/bookings.html', {'page_obj': page_obj})


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

    paginator = Paginator(clients, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'managers/pages/search_list.html',
        {'form': form, 'page_obj': page_obj},
    )
