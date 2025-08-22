from django.contrib import admin
from users.models import UserModel

# Register your models here.


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
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
