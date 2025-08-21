from django.contrib import admin
from users.models import UserModel

# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "email",
        "is_active",
        "role",
    )
    list_display_links = (
        "name",
        "surname",
        "email",
        "is_active",
        "role",
    )
    search_fields = (
        "name",
        "surname",
        "email",
    )
