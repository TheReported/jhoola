from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from hotel.models import Hotel
from users.models import Client
import json


@csrf_exempt
@require_POST
def user_login(request, hotel_slug):
    data = json.loads(request.body)
    username, password = data['username'], data['password']

    try:
        hotel = Hotel.objects.get(slug=hotel_slug)
    except Hotel.DoesNotExist:
        return HttpResponse('Error: Hotel does not exist', status=404)

    try:
        Client.objects.select_related('user').get(user__username=username, hotel=hotel)
    except Client.DoesNotExist:
        return HttpResponse('Error: This user is not associated with this hotel.', status=403)

    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponse('Error: Invalid username or password.', status=401)

    return HttpResponse(f'Login successful for user: {username} at {hotel.name}', status=200)


# def dashboard(request):
#     return render(request, 'users/dashboard.html', {})
