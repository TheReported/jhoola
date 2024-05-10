from django import forms

from .models import Product


class ProductCreationForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    price = forms.DecimalField(label='Price', min_value=0, initial=Product._meta.get_field('price').default) 
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class ProductEditForm(forms.ModelForm):
    price = forms.DecimalField(label='Price', min_value=0,initial=Product._meta.get_field('price').default) 
    class Meta:
        model = Product
        fields = ['name', 'price']
