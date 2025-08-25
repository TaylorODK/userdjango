from api.serializers.models.product import ProductSerializer
from api.serializers.responses.base import (
    BaseResponseSerializer,
    ErrorResponseSerializer,
)


class ProductResponseSerializer(BaseResponseSerializer):
    """Сериализатор для ответа на запрос по продуктам."""

    data = ProductSerializer()


class ProductErrorResponseSerializer(ErrorResponseSerializer):
    """Сериализатор для ответа с ошибками продуктов"""

    pass
