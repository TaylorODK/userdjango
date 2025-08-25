from http import HTTPStatus

from drf_spectacular.utils import OpenApiResponse, extend_schema

from api.serializers import (
    UserCreateResponseSerializer,
    UserResponseSerializer,
    UserErrorResponseSerializer,
    UserCreateSerializer,
)

user_create_schema = extend_schema(
    operation_id="user_create_schema",
    description="Создание нового пользователя",
    summary="Регистрация пользователя",
    tags=["User"],
    request=UserCreateSerializer,
    responses={
        HTTPStatus.CREATED: OpenApiResponse(
            description="Пользователь успешно создан",
            response=UserCreateResponseSerializer,
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка создания пользователя",
            response=UserErrorResponseSerializer,
        ),
        HTTPStatus.UNAUTHORIZED: OpenApiResponse(
            description="Неавторизованных запрос",
            response=UserErrorResponseSerializer,
        ),
    },
)


user_content_schema = extend_schema(
    operation_id="user_content_schema",
    description="Данные о пользователях",
    summary="Получение данных о пользователях",
    tags=["User"],
    responses={
        HTTPStatus.OK: OpenApiResponse(
            description="Данные пользователя получены",
            response=UserResponseSerializer,
        ),
        HTTPStatus.BAD_REQUEST: OpenApiResponse(
            description="Ошибка получения данных пользователей",
            response=UserErrorResponseSerializer,
        ),
        HTTPStatus.UNAUTHORIZED: OpenApiResponse(
            description="Неавторизованных запрос",
            response=UserErrorResponseSerializer,
        ),
        HTTPStatus.FORBIDDEN: OpenApiResponse(
            description="Недостаточно прав",
            response=UserErrorResponseSerializer,
        ),
    },
)
