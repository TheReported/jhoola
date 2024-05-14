from django.contrib import messages
from django.shortcuts import redirect, render

from users.forms import SupportForm
from users.tasks import contact_support

from .forms import HotelForm


def main(request):
    if request.user.is_staff:
        return redirect("admin:index")
    if request.user.is_authenticated:
        if request.user.groups.filter(name='HotelManagers').exists():
            return redirect('users:manager_dashboard')
        return redirect('booking:booking_list', username=request.user.username)
    if request.method == 'POST':
        hotel_form = HotelForm(request.POST)
        support_form = SupportForm(request.POST)
        if hotel_form.is_valid():
            hotel_selector = hotel_form.cleaned_data['hotel_selector']
            hotel_name = hotel_selector.split(',')[0].strip()
            request.session['hotel_session_name'] = hotel_name
            request.session.save()
            return redirect('user_login')
        if support_form.is_valid():
            cd = support_form.cleaned_data
            contact_support.delay(cd)
    else:
        hotel_form = HotelForm()
        support_form = SupportForm()
    return render(request, 'main.html', {'form': hotel_form, 'support_form': support_form})
