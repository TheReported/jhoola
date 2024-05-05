from django.contrib.auth.models import User
from django.test import TestCase

from .forms import ClientEditForm, ClientRegistrationForm


class ClientFormTests(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'username': 'testuser',
            'password': 'xd1234Tfe',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'num_guest': '2',
        }
        form = ClientRegistrationForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form_data = {
            'username': '',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
        }
        form = ClientRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_valid_edit_form(self):
        user = User.objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='maradonaT20',
        )
        form_data = {
            'username': 'testuser',
            'first_name': 'New',
            'last_name': 'Name',
            'email': 'test@example.com',
            'password': 'maradonaT20',
            'num_guest': '4',
        }
        form = ClientEditForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())

    def test_invalid_edit_form(self):
        user = User.objects.create(
            username='testuser', first_name='Test', last_name='User', email='test@example.com'
        )
        form_data = {
            'username': '',
            'first_name': 'New',
            'last_name': 'Name',
            'email': 'test@example.com',
        }
        form = ClientEditForm(data=form_data, instance=user)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
