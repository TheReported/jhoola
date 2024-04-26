from django import forms
from django_svg_image_form_field import SvgAndImageFormField
from .models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class SvgIconForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
        field_classes = {
            'avatar': SvgAndImageFormField,
        }
