from django.contrib import admin
from users.models import UserModel, Role, AccessRolesRule

# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    """Админка для редактирования пользователей."""

    list_display = (
        "first_name",
        "last_name",
        "email",
        "is_active",
        "role",
    )
    list_display_links = (
        "first_name",
        "last_name",
        "email",
        "is_active",
        "role",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    """Админка для редактирования ролей."""

    list_display = (
        "name",
        "slug",
        "description",
    )
    list_display_links = ("name",)
    search_fields = ("name",)


@admin.register(AccessRolesRule)
class AccessRolesRuleAdmin(admin.ModelAdmin):
    """Админка для редактирования доступа."""

    list_display = ("role", "element")
    list_display_links = ("role", "element")
    search_fields = ("role", "element")
