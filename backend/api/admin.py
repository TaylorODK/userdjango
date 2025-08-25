from django.contrib import admin
from .models import Order, Product

# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для включения в админку модели Order."""

    list_display = ("name", "description", "user", "date_order")
    search_fields = ("user",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для включения в админку модели Product."""

    list_display = ("name", "slug", "description")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
