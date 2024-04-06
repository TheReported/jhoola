from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Hotel
from .forms import HotelForm


def main(request):
    form = HotelForm()
    return render(request, 'main.html', {'form': form})


def get_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['hotel_selector'])
            hotel = get_object_or_404(Hotel, name=cd['name'])
            return redirect(reverse('login', kwargs={'hotel_slug': hotel.slug}))
    else:
        form = HotelForm()
    return render(request, 'main.html', {'form': form})
