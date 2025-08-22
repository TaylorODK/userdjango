from django.contrib.auth.models import AbstractUser
from django.db import models
from effictivemobile.constants import (
    NAME_MAX_LENGTH,
    PASSWORD_MAX_LENGTH,
    USERS_ROLE,
    USER,
    MODERATOR,
    ADMIN,
)


class UserModel(AbstractUser):
    """Кастомная модель пользователя."""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        help_text="Введите адрес электронной почты",
        unique=True,
    )
    role = models.CharField(
        choices=USERS_ROLE,
        default=USER,
        verbose_name="Роль пользователя",
        help_text="Данные о роли пользователя (user по-умолчанию)",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_admin(self):
        return self.role == ADMIN or self.is_superuser

    def is_moderator(self):
        return self.role == MODERATOR

    def is_user(self):
        return self.role == USER
