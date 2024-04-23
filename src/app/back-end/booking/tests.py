from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from hotel.models import Hotel

from .models import Booking, Client, Product


class BookingTestCase(TestCase):
    def test_booking_creation(self):
        user = User.objects.create(
            username="ejemplo_usuario", first_name="Ejemplo", last_name="Usuario"
        )
        hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')
        client = Client.objects.create(user=user, num_guest=2, hotel=hotel)
        product1 = Product.objects.create(name="Producto 1", price=10.00, hotel=hotel)
        product2 = Product.objects.create(name="Producto 2", price=15.00, hotel=hotel)

        booking = Booking.objects.create(
            user=client,
            price=25.00,
            duration=Booking.TimeSlots.MORNING,
            date=datetime.now().date(),
            paid=False,
        )
        booking.products.add(product1, product2)

        self.assertEqual(booking.user, client)
        self.assertEqual(booking.price, 25.00)
        self.assertEqual(booking.duration, Booking.TimeSlots.MORNING)
        self.assertFalse(booking.paid)
        self.assertEqual(booking.products.count(), 2)

    def test_booking_duration(self):
        hotel = Hotel.objects.create(name='Test Hotel', city='Test Location')

        user = User.objects.create(
            username="ejemplo_usuario", first_name="Ejemplo", last_name="Usuario"
        )
        client = Client.objects.create(user=user, num_guest=2, hotel=hotel)

        morning_booking = Booking.objects.create(
            user=client,
            price=10.00,
            duration=Booking.TimeSlots.MORNING,
            date=datetime.now().date(),
            paid=False,
        )
        afternoon_booking = Booking.objects.create(
            user=client,
            price=15.00,
            duration=Booking.TimeSlots.AFTERNOON,
            date=datetime.now().date(),
            paid=False,
        )
        all_day_booking = Booking.objects.create(
            user=client,
            price=25.00,
            duration=Booking.TimeSlots.ALL_DAY,
            date=datetime.now().date(),
            paid=False,
        )

        self.assertEqual(morning_booking.duration, Booking.TimeSlots.MORNING)
        self.assertEqual(afternoon_booking.duration, Booking.TimeSlots.AFTERNOON)
        self.assertEqual(all_day_booking.duration, Booking.TimeSlots.ALL_DAY)
