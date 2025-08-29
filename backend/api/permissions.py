from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from users.models import AccessRolesRule, Role


def check_permission_for_current_user(request, view):
    """
    Функция для получения объекта модели AccessRolesRule.
    """
    user = request.user
    element = view.queryset.model._meta.model_name
    if not user.is_authenticated:
        role = Role.objects.get(slug="guest")
    else:
        role = user.role
    try:
        return AccessRolesRule.objects.get(role=role, element__slug=element)
    except AccessRolesRule.DoesNotExist:
        return None


class AccessPermission(permissions.BasePermission):
    """
    Проверки уровня доступа для пользователей.
    Если пользователь не авторизован,
    то ему предоставляется доступ для роли "Гость".
    """

    def has_permission(self, request, view):
        access = check_permission_for_current_user(request, view)
        if not access:
            return False
        if request.method in SAFE_METHODS:
            return access.read_all_permission
        if request.method == "POST":
            return access.create_permission
        return False

    def has_object_permission(self, request, view, obj):
        access = check_permission_for_current_user(request, view)
        if not access:
            return False
        if request.method in SAFE_METHODS:
            return access.read_permission
        obj_user = getattr(obj, "user", None)
        if obj_user and request.user == obj_user:
            if request.method in ("PATCH", "PUT"):
                return access.update_permission
            if request.method == "DELETE":
                return access.delete_permission
        if request.method == "POST":
            return access.create_permission
        elif request.method in ("PATCH", "PUT"):
            return access.update_all_permission
        elif request.method == "DELETE":
            return access.delete_all_permission
        return False
