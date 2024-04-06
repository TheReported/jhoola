from django.contrib.auth.forms import AuthenticationForm
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import HotelForm
from .models import Hotel


def main(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            hotel = get_object_or_404(Hotel, name=cd['name'])
            return redirect(reverse('login', kwargs={'hotel_slug': hotel.slug}))
    else:
        hotel = Hotel.objects.last()
        form = HotelForm()
    return render(request, 'main.html', {'form': form, 'hotel': hotel})
