from http import HTTPStatus

from drf_spectacular.utils import OpenApiResponse, extend_schema

from api.serializers import (
    OrderResponseSerializer,
    OrderErrorResponseSerializer,
    OrderSerializer,
)


order_content_schema = extend_schema(
    operation_id="order_content",
    summary="Получить данные о заказе",
    description="Получение данных заказа",
    tags=["Order"],
    responses={
        HTTPStatus.OK: OpenApiResponse(
            description="Контент успешно получен", response=OrderResponseSerializer
        ),
        HTTPStatus.CREATED: OpenApiResponse(
            description="Заказ успешно создан", response=OrderResponseSerializer
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка валидации входных данных",
            response=OrderErrorResponseSerializer,
        ),
    },
)

order_create_schema = extend_schema(
    operation_id="order_create_content",
    summary="Создание заказа",
    description="Создание нового заказа",
    tags=["Order"],
    request=OrderSerializer,
    responses={
        HTTPStatus.CREATED: OpenApiResponse(
            description="Заказ успешно создан", response=OrderResponseSerializer
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка валидации входных данных",
            response=OrderErrorResponseSerializer,
        ),
        HTTPStatus.FORBIDDEN: OpenApiResponse(
            description="Ошибка доступа", response=OrderErrorResponseSerializer
        ),
    },
)
