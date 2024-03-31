from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from hotel.models import Hotel
from users.models import Client
from product.models import Product
from booking.models import Booking
from django.shortcuts import redirect, render
import json
from .decorators import is_hotel_manager


@csrf_exempt
@require_POST
def user_login(request, hotel_slug):
    data = json.loads(request.body)
    username, password = data['username'], data['password']

    try:
        hotel = Hotel.objects.get(slug=hotel_slug)
    except Hotel.DoesNotExist:
        return HttpResponse('Hotel does not exist', status=404)

    try:
        client = Client.objects.select_related('user').get(user__username=username, hotel=hotel)
    except Client.DoesNotExist:
        return HttpResponse('This user is not associated with this hotel.', status=403)

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        if user.groups.filter(name='HotelManager').exists():
            return redirect('users:dashboard')

        return JsonResponse(
            {'client_id': client.id, 'username': username, 'password': password, 'status': 200}
        )
    return HttpResponse('Invalid username or password.', status=401)


@is_hotel_manager
def dashboard(request, hotel_slug):
    clients = Client.objects.filter(hotel__slug=hotel_slug)
    products = Product.objects.filter(hotel__slug=hotel_slug)
    bookings = Booking.objects.filter(hotel__slug=hotel_slug)
    return render(
        request,
        'managers/dashboard-manager.html',
        {'clients': clients, 'products': products, 'bookings': bookings},
    )
