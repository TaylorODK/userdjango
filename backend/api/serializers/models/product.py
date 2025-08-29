from rest_framework import serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продуктов."""

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        fields = ("id", "name", "slug", "price", "description")
