from django import forms
from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'num_guest',
        'telephone',
        # 'name_surname',
        # 'email',
        # 'last_login',
        'hotel',
    ]
    raw_id_fields = ['user', 'hotel']
    list_filter = ['hotel']
