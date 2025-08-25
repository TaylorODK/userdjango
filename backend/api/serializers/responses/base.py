from rest_framework import serializers


class BaseResponseSerializer(serializers.Serializer):
    """Базовый сериализатор для успешных ответов."""

    succes = serializers.BooleanField(
        help_text="Статус успешности операции", default=True
    )
    message = serializers.CharField(help_text="Сообщение об операции")
    data = serializers.JSONField(help_text="Данные операции", required=False)


class ErrorResponseSerializer(serializers.Serializer):
    """Базовый сериализатор для ошибки."""

    succes = serializers.BooleanField(
        help_text="Статус успешности операции", default=False
    )
    message = serializers.CharField(help_text="Сообщение об ошибке")
    errors = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField(),
            help_text="Список ошибок для конкретного поля",
        ),
        help_text="Словарь ошибок валидации, где ключ - название поля, "
        "значение - список ошибок",
        required=False,
        allow_empty=True,
    )
