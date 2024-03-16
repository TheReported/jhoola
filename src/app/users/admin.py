from django.contrib import admin

from .models import NewUser


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'num_guest', 'hotel']
    raw_id_fields = ['hotel']
    list_filter = ['hotel']
