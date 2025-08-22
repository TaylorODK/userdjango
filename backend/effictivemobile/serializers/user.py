from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from users.models import UserModel


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор обновления данных о пользователе (имя и фамилия).
    """

    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "repeat_password",
        )

    def validate(self, data):
        password = data.get("password")
        repeat_password = data.get("repeat_password")
        if password != repeat_password:
            raise serializers.ValidationError(
                "Введите дважды одинаковый пароль"
            )
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(
                {
                    "Пароль не соответствует требования безопасности": list(
                        e.messages
                    )
                }
            )
        return data

    def create(self, validated_data):
        validated_data.pop("repeat_password")
        password = make_password(validated_data.get("password"))
        user = UserModel.objects.create(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data.get("email"),
            password=password
        )
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор обновления данных о пользователе (имя и фамилия).
    """

    class Meta:
        model = UserModel
        fields = ("id", "first_name", "last_name",)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = UserModel.objects.get(email=email)
        if not user:
            raise ValidationError({"Пользователя не существует"})
        try:
            user.check_password(password)
        except ValidationError:
            raise ValidationError({"Неверный пароль"})
        return data
