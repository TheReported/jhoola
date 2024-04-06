from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClientCreationForm, ClientUpdateForm
from .models import Client, Hotel
from django.contrib.auth import authenticate, login

from .forms import LoginForm


def user_login(request):
    selected_hotel = request.session.get('hotel_session_name')
    print(selected_hotel)
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
                    if user.groups.filter(name='admin-hotel').exists():
                        return redirect(manager_dashboard)
                    return redirect(client_dashboard)
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, 'selected_hotel': selected_hotel})


def client_dashboard(request):
    return render(request, 'users/dashboard.html', {})


def manager_dashboard(request):
    return render(request, 'managers/dashboard-manager.html', {})


def create_client(request):
    if request.method == 'POST':
        clientcreation_form = ClientCreationForm(request.POST)
        if clientcreation_form.is_valid():
            clientcreation_form.save()
            messages.success(request, 'Your client has been created successfully.')
            # return redirect('')
        messages.error(request, 'Error! Your client could not be created')
    else:
        clientcreation_form = ClientCreationForm()
    # return   render(request, '', {'clientcreation_form': clientcreation_form})


def update_client(request, user):
    instance = get_object_or_404(Client, user=user)
    if request.method == 'POST':
        clientupdate_form = ClientUpdateForm(request.POST, instance=instance)
        if clientupdate_form.is_valid():
            clientupdate_form.save()
            messages.success(request, 'Your client has been updated successfully.')
            # return redirect('')
        messages.error(request, 'Error! Your client could not be updated')
    else:
        clientupdate_form = ClientUpdateForm(instance=instance)
    # return render(request, '', {'clientupdate_form': clientupdate_form})


def delete_client(request, user):
    client = get_object_or_404(Client, user=user)
    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Your client has been deleted successfully.')
        # return redirect('')
    # return render(request, '', {'client': client})


def client_list(request, hotel_code):
    hotel = Hotel.objects.get(code=hotel_code)
    clients = Client.objects.filter(hotel=hotel)
    # return render(request, '', {'clients': clients})
