from django.http import HttpResponseBadRequest
def is_hotel_manager(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='HotelManager').exists():
            return function(request, *args, **kwargs)
        return HttpResponseBadRequest('You must be an Hotel Manager')

    return wrapper
