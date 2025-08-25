from http import HTTPStatus

from drf_spectacular.utils import OpenApiResponse, extend_schema

from api.serializers import (
    ProductResponseSerializer,
    ProductErrorResponseSerializer,
    ProductSerializer,
)

product_content_schema = extend_schema(
    operation_id="product_content",
    summary="Получить контент страницы продуктов",
    description="Получение контента страницы продуктов",
    tags=["Product"],
    responses={
        HTTPStatus.OK: OpenApiResponse(
            description="Контент успешно получен",
            response=ProductResponseSerializer,
        ),
        HTTPStatus.CREATED: OpenApiResponse(
            description="Контент успешно создан", response=ProductResponseSerializer
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка получения данных",
            response=ProductErrorResponseSerializer,
        ),
    },
)

product_create_schema = extend_schema(
    operation_id="product_create",
    summary="Добавление продукта",
    description="Создание страницы продукта",
    tags=["Product"],
    request=ProductSerializer,
    responses={
        HTTPStatus.CREATED: OpenApiResponse(
            description="Контент успешно создан", response=ProductResponseSerializer
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка создания страницы",
            response=ProductErrorResponseSerializer,
        ),
        HTTPStatus.FORBIDDEN: OpenApiResponse(
            description="Ошибка доступа",
            response=ProductErrorResponseSerializer,
        ),
    },
)
