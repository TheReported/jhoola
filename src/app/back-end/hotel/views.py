from django.shortcuts import render, redirect
from .forms import HotelForm

def main(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel_selector = form.cleaned_data['hotel_selector']
            hotel_name = hotel_selector.split(',')[0].strip()
            request.session['hotel_session_name'] = hotel_name
            request.session.save()
            return redirect('user_login')
    else:
        form = HotelForm()
    return render(request, 'main.html', {'form': form})
