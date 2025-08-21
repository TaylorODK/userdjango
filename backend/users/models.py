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

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Фамилия пользователя",
        help_text="Введите фамилию пользователя",
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты",
        help_text="Введите адрес электронной почты",
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        verbose_name="Пароль",
        help_text="Введите пароль",
    )
    passord_again = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        verbose_name="Повтор пароля",
        help_text="Повторное введите пароль",
    )
    registation_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата регистрации пользователя",
    )
    is_active = models.BooleanField(
        verbose_name="Информация об активности аккаунта",
        default=True,
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
        return f"{self.name} {self.surname}"

    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    def is_moderator(self):
        return self.role == self.MODERATOR

    def is_user(self):
        return self.role == self.USER
