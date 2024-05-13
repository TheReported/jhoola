from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'show_products', 'duration', 'price', 'date', 'paid']

    def show_products(self, obj):
        return ', '.join([str(product) for product in obj.products.all()])

    show_products.short_description = 'Products'
