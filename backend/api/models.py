from django.db import models
from users.models import UserModel

from effictivemobile.constants import (
    NAME_MAX_LENGTH,
    PRICE_DECIMAL_PLACES,
    PRICE_MAX_DIGITS,
)
from django.utils.timezone import now as NOW
from .mixins import AutoSlugMixin

# Create your models here.


class Product(AutoSlugMixin, models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=False,
        verbose_name="Наименование продукта",
        help_text=f"Максимальная длина наименования {NAME_MAX_LENGTH}",
    )
    slug = models.SlugField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        verbose_name="Слаг продукта",
        help_text="Слаг автоматически генерируется на основании поля name",
    )
    description = models.TextField(
        blank=True, verbose_name="Описание продукта"
    )
    price = models.DecimalField(
        blank=False,
        verbose_name="Стоимость продукта",
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"Продукт {self.name}, стоимостью {self.price} рублей."


class Order(models.Model):
    """Модель заказа."""

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=False)
    date_order = models.DateField(
        blank=False,
        verbose_name="Дата заказа",
        help_text="Укажите дату заказа в формате DD.MM.YYYY",
        default=NOW,
    )
    products = models.ManyToManyField(
        Product, blank=False, verbose_name="Продукты"
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ {self.user}"

    def total_price(self):
        return sum(product.price for product in self.products.all())
