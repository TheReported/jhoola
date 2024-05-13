import random
import string
from django.utils import timezone
import calendar
from booking.models import Booking
from hotel.models import Hotel


def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(8))


def get_monthly_bookings(hotel: Hotel) -> list:
    month_first_day = timezone.now().date().replace(day=1)
    month_last_day = month_first_day.replace(
        day=calendar.monthrange(month_first_day.year, month_first_day.month)[1]
    )
    bookings = Booking.objects.filter(
        user__hotel=hotel, paid=True, date__range=(month_first_day, month_last_day)
    )

    return bookings
