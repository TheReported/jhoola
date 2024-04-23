from django.test import TestCase

from .forms import ProductCreationForm, ProductEditForm
from .models import Hotel, Product


class ProductModelTestCase(TestCase):
    def test_product_model(self):
        self.hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')

        product = Product.objects.create(name='Test Product', price=50.00, hotel=self.hotel)

        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 50.00)
        self.assertEqual(product.hotel, self.hotel)
        self.assertEqual(product.status, Product.Status.FREE)


class ProductFormTestCase(TestCase):
    def test_product_form_valid_data(self):
        self.hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')
        form = ProductCreationForm(data={'name': 'Producto 1', 'price': 10.99, 'hotel': self.hotel})

        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = ProductCreationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class ProductEditFormTestCase(TestCase):

    def test_product_edit_form_valid_data(self):
        self.hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')
        product = Product.objects.create(name='Producto 1', price=10.99, hotel=self.hotel)
        form = ProductEditForm(
            instance=product,
            data={'name': 'Producto Editado', 'price': 15.99, 'hotel': self.hotel.id},
        )

        self.assertTrue(form.is_valid())

    def test_product_edit_form_no_data(self):
        hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')
        product = Product.objects.create(name='Producto 1', price=10.99, hotel=hotel)
        form = ProductEditForm(instance=product, data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
