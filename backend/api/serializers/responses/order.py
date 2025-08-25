from api.serializers.models.order import OrderSerializer
from api.serializers.responses.base import (
    BaseResponseSerializer,
    ErrorResponseSerializer,
)


class OrderResponseSerializer(BaseResponseSerializer):
    """Сериализатор для ответа на запрос по заказам."""

    data = OrderSerializer()


class OrderErrorResponseSerializer(ErrorResponseSerializer):
    """Сериализатор для ответа с ошибками при заказах."""

    pass
