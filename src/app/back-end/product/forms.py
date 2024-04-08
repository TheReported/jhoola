from django import forms

from .models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
