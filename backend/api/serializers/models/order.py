from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from api.models import Order, Product
from codescommanders.constants import PRICE_MAX_DIGITS, PRICE_DECIMAL_PLACES
import datetime


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели заказа."""

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True
    )
    slug = serializers.SlugField(read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "name",
            "slug",
            "description",
            "user",
            "date_order",
            "products",
            "price",
        )

    @extend_schema_field(
        serializers.DecimalField(
            max_digits=PRICE_MAX_DIGITS, decimal_places=PRICE_DECIMAL_PLACES
        )
    )
    def get_price(self, obj):
        return sum(product.price for product in obj.products.all())

    def validate(self, data):
        date_order = data.get("date_order")
        if date_order and datetime.date.today() > date_order:
            raise serializers.ValidationError("Нельзя выбрать дату заказа в прошлом.")
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        products = validated_data.pop("product", [])
        order = Order.objects.create(**validated_data, user=request.user)
        order.product.set(products)
        return order
