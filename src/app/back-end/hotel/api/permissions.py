from rest_framework.permissions import BasePermission

class PublicGetOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'
