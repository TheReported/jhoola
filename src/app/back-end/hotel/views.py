from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import HotelForm
from .models import Hotel


@csrf_exempt
def main(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")
    print(request.method)
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            hotel = get_object_or_404(Hotel, name=cd['name'])
            print(hotel)
            return redirect(reverse('login', kwargs={'hotel_slug': hotel.slug}))
    else:
        hotel = Hotel.objects.last()
        form = HotelForm()
    return render(request, 'main.html', {'form': form, "hotel": hotel})
