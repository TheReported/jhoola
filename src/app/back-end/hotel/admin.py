from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'city', 'country', 'email', 'phone', 'code', 'site_map']
    prepopulated_fields = {'slug': ('name',)}
