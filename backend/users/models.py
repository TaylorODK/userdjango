from django.contrib.auth.models import AbstractUser
from django.db import models
from effictivemobile.constants import (
    NAME_MAX_LENGTH,
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
    role = models.ForeignKey(
        "Role",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_role_slug(self):
        return self.role.slug if self.role else "guest"


class Role(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Наименование роли",
        unique=True,
    )
    slug = models.SlugField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Слаг",
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание роли",
    )

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class BusinessElements(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Наименование ресурса",
        unique=True,
    )
    slug = models.SlugField(
        max_length=NAME_MAX_LENGTH,
        verbose_name="Слаг",
        unique=True,
    )
    description = models.TextField(verbose_name="Описание ресурса")


class AccessRolesRules(models.Model):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )
    element = models.ForeignKey(
        BusinessElements,
        on_delete=models.CASCADE,
    )
    read_permission = models.BooleanField(
        verbose_name="Доступ для чтения собственного объекта модели",
        default=False,
    )
    read_all_permission = models.BooleanField(
        verbose_name="Доступ для чтения всех объектов модели",
        default=False,
    )
    create_permission = models.BooleanField(
        verbose_name="Доступ для создания объекта модели",
        default=False,
    )
    update_permission = models.BooleanField(
        verbose_name="Возможность редактирования собственного объекта модели",
        default=False,
    )
    update_all_permission = models.BooleanField(
        verbose_name="Возможность редактирования всех объектов модели",
        default=False,
    )
    delete_permission = models.BooleanField(
        verbose_name="Возможность удаления собственного объекта модели",
        default=False,
    )
    delete_all_permission = models.BooleanField(
        verbose_name="Возможность удаления всех объектов модели",
        default=False,
    )

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"

    def __str__(self):
        return (
            f"Доступ роли '{self.role.name}' к объекту '{self.element.name}'."
        )
