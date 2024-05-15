from django.contrib import admin

from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'city',
        'country',
        'email',
        'phone',
        'code',
        'opening_morning_hours',
        'opening_afternoon_hours',
    ]
    search_fields = ['name', 'city', 'country']
    prepopulated_fields = {'slug': ('name',)}

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['opening_morning_hours'].widget.attrs['placeholder'] = 'hh:mm - hh:mm'
        form.base_fields['opening_afternoon_hours'].widget.attrs['placeholder'] = 'hh:mm - hh:mm'
        return form
