from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductCreationForm, ProductUpdateForm
from .models import Hotel, Product


def create_product(request):
    if request.method == 'POST':
        productcreation_form = ProductCreationForm(request.POST)
        if productcreation_form.is_valid():
            productcreation_form.save()
            messages.success(request, 'Your product has been created successfully.')
            # return redirect('')
        messages.error(request, 'Error! Your product could not be created')
    else:
        productcreation_form = ProductCreationForm()
    # return   render(request, '', {'productcreation_form': productcreation_form})


def update_product(request, user):
    instance = get_object_or_404(Product, user=user)
    if request.method == 'POST':
        productupdate_form = ProductUpdateForm(request.POST, instance=instance)
        if productupdate_form.is_valid():
            productupdate_form.save()
            messages.success(request, 'Your product has been updated successfully.')
            # return redirect('')
        messages.error(request, 'Error! Your product could not be updated')
    else:
        productupdate_form = ProductUpdateForm(instance=instance)
    # return render(request, '', {'productupdate_form': productupdate_form})


def delete_product(request, user):
    product = get_object_or_404(Product, user=user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Your product has been deleted successfully.')
        # return redirect('')
    # return render(request, '', {'product': product})


def product_detail(request, user):
    product = get_object_or_404(Product, user=user)
    # return render(request, '', {'product': product})


def Product_list(request, hotel_code):
    hotel = Hotel.objects.get(code=hotel_code)
    products = Product.objects.filter(hotel=hotel)
    # return render(request, '', {'products': products})
