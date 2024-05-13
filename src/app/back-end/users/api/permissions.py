from rest_framework import permissions


class AdminSiteAccess(permissions.BasePermission):
    message = "You don't have any permissions for entry on this API."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.groups.filter(name='HotelManagers').exists()
        )
