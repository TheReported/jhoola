from django.shortcuts import render, get_object_or_404
from .models import Hotel
from .forms import HotelForm


def main(request):
    form = HotelForm()
    return render(request, 'main.html', {'form': form})


# class HotelAutoComplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = Hotel.objects.all()
#         name_filter = qs.filter(name__icontains=self.q)
#         city_filter = qs.filter(city__icontains=self.q)
#         return name_filter | city_filter if self.q else qs


def get_hotels(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            hotel = get_object_or_404(Hotel, name=cd['name'])
            return hotel.slug
    else:
        form = HotelForm()
    return render(request, 'main.html', {'form': form})
