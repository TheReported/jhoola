from django.shortcuts import get_object_or_404, redirect, render
from .forms import ClientRegistrationForm
from .models import Client, Hotel
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


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
                    return redirect('users:client_dashboard', username=user.username)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def client_dashboard(request, username):
    client = get_object_or_404(Client, user=request.user)
    return render(request, 'users/dashboard.html', {'client': client})


@login_required
def manager_dashboard(request):
    client = get_object_or_404(Client, user=request.user)
    return render(request, 'managers/dashboard-manager.html', {'client': client})


def register(request):
    if request.method == 'POST':
        user_form = ClientRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password']) # TODO: Ajustar tema de contraseña automática 
            new_user.save()
            Client.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
        else:
            return render(request, 'managers/pages/users.html', {'user_form': user_form})
    else:
        user_form = ClientRegistrationForm()
    return render(request, 'managers/pages/users.html', {'user_form': user_form})