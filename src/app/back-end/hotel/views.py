from django.shortcuts import redirect, render

from .forms import HotelForm


def main(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='HotelManagers').exists():
            return redirect('users:manager_dashboard')
        return redirect('users:client_dashboard', username=request.user.username)
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
