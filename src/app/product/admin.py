from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'avatar', 'status', 'hotel']
    raw_id_fields = ['hotel']
    prepopulated_fields = {'slug': ('name',)}
