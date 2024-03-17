from django.contrib import admin

from .models import NewUser

fields = [
    'username',
    'email',
    'num_guest',
    'hotel',
    'groups',
    'user_permissions',
    'is_active',
]


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'num_guest', 'hotel']
    raw_id_fields = ['hotel']
    list_filter = ['hotel']
    fields = fields
