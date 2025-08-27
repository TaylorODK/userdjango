from django.contrib import admin
from .models import Order, Product

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для включения в админку модели Order."""

    list_display = ("user", "date_order", "total_price")
    search_fields = ("user",)

    @admin.display(description="Цена заказа")
    def total_price(self, obj):
        return obj.total_price()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для включения в админку модели Product."""

    list_display = ("name", "slug", "description")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
