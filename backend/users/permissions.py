from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    """"
    Разрешения для операций с моделью пользователей.
    Разрешается просмотр/редактирование/пользователей,
    а также просмотр списка пользователей для администраторов.
    Разрешается просмотр/редактирование/удаление/смена пароля
    собственного профиля.
    Неавторизованным пользователям запрещены все операции.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if not request.user.is_authenticated:
            return False
        if request.user.is_role_slug() == "admin" or obj.pk == request.user.pk:
            return True
