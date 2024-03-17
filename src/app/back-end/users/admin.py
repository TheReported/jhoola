from django import forms
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


class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True


@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'num_guest', 'hotel']
    raw_id_fields = ['hotel']
    list_filter = ['hotel']
    fields = fields
    form = NewUserForm
