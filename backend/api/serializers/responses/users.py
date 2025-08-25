from api.serializers.models.users import UserCreateSerializer, UserSerializer
from api.serializers.responses.base import (
    BaseResponseSerializer,
    ErrorResponseSerializer,
)


class UserCreateResponseSerializer(BaseResponseSerializer):
    """Сериализатор для ответа на запрос по созданию пользователей."""

    data = UserCreateSerializer()


class UserResponseSerializer(BaseResponseSerializer):
    """Сериализатор для ответа на запрос по пользователям."""

    data = UserSerializer()


class UserErrorResponseSerializer(ErrorResponseSerializer):
    """Сериализатор для ответа с ошибками по пользователям."""

    pass
