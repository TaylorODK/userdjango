from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import GenericViewSet
from users.models import UserModel, BusinessElement, Role, AccessRolesRule
from users.serializers import (
    UserChangePasswordSerializer,
    UserCreateSerializer,
    UserDeleteSerializer,
    UserUpdateSerializer,
    UserShowSerializer,
    RoleSerializer,
    BusinessElementSerializer,
    AccessChangeSerializer,
    AccessShowSerializer,
)
from users.permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для пользователей.
    Предусмотрена возможность создания пользователя
    для неавторизованных пользователей.
    Администраторам доступна возможность по просмотру/редактированию
    пользователей, а также  просмотр списка пользователей
    Для авторизованных пользователей доступна
    возможность просмотра/редактирования/удаления/смены пароля
    собственного профиля.
    Также авторизованным пользователям доступна возможность просмотра
    доступов к моделям по ссылке me/permissions/{наименование модели}
    """
    queryset = UserModel.objects.all()
    serializer_class = UserShowSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny(),]
        return [UserPermission(),]

    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception:
                return Response({"Ошибка создания пользователя."})
            return Response(
                {
                    "Success": True,
                    "Message": "Пользователь успешно создан.",
                    "Data": serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=["get", "patch"],
        url_path="me",
    )
    def me_page(self, request):
        user = self.request.user
        if request.method == "get":
            try:
                serializer = UserShowSerializer(user)
            except Http404:
                return Response(
                    {
                        "Success": False,
                        "Message": "Информация о пользователе недоступна.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            return Response(
                    {
                        "Success": True,
                        "Message": "Предоставлены данные пользователя.",
                        "Data": serializer.data
                    },
                    status=status.HTTP_200_OK,
                )
        serializer = UserUpdateSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Success": True,
                    "Message": "Данные пользователя успешно изменены.",
                    "Data": serializer.data
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "Success": False,
                "Message": "Ошибка смены данных пользователя",
                "Data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        detail=False,
        methods=["patch"],
        url_path="me/delete"
    )
    def delete_user(self, request):
        user = self.request.user
        serializer = UserDeleteSerializer(
            user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Success": True,
                    "Message": "Пользователь удален.",
                    "Data": serializer.data
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "Success": False,
                "Message": "Ошибка удаления пользователя",
                "Data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        detail=False,
        methods=["PATCH"],
        url_path="me/change-password",
    )
    def change_password(self, request):
        user = self.request.user
        serializer = UserChangePasswordSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "Success": True,
                    "Message": "Пароль изменен."
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "Success": False,
                "Message": "Ошибка смена пароля",
                "Data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        detail=False,
        methods=["GET"],
        url_path=r"me/permissions/(?P<model_name>[^/.]+)"
    )
    def me_permissions(self, request, model_name):
        user = self.request.user
        try:
            access = AccessRolesRule.objects.get(role=user.role, element__slug=model_name)
        except AccessRolesRule.DoesNotExist:
            return Response(
                {
                    "Success": False,
                    "Message": "Данные о правах доступа не обнаружены."
                }
            )
        serializer = AccessShowSerializer(access)
        if serializer:
            return Response(
                {
                    "Success": True,
                    "Message": "Пользователь удален.",
                    "Data": serializer.data
                },
                status=status.HTTP_200_OK,
            )
