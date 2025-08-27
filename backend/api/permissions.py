from rest_framework import permissions
from users.models import AccessRolesRule

class AccessPermissions(permissions.BasePermission):
    """Проверка пользователя на авторство объека."""

    def has_object_permission(self, request, view, obj):
        if request.method == "get":
            return 
        return request.method in permissions.SAFE_METHODS or obj.user == request.user
