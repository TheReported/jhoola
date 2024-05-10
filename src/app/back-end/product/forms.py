from django import forms

from .models import Product


class ProductCreationForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
