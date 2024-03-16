from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'duration', 'price', 'timestamp']
    raw_id_fields = ['user', 'product']
