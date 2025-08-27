from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from users.models import UserModel


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания нового пользователя.
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
            raise serializers.ValidationError("Введите дважды одинаковый пароль")
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(
                {"Пароль не соответствует требования безопасности": list(e.messages)}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("repeat_password")
        password = make_password(validated_data.get("password"))
        user = UserModel.objects.create(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data.get("email"),
            password=password,
        )
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор обновления данных о пользователе (имя, фамилия, почта).
    """

    class Meta:
        model = UserModel
        fields = ("id", "first_name", "last_name", "email")

    def validate(self, value):
        user = self.instance
        if UserModel.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise ValidationError({"Адрес электронной почты занят"})
        return value


class UserDeleteSerializer(serializers.ModelSerializer):
    """
    Сериализатор мягкого удаления пользователя.
    """

    class Meta:
        model = UserModel
        fields = ("id", "email", "password")

    def validate_current_password(self, value):
        user = self.instance
        if not user.check_password(value):
            raise serializers.ValidationError("Неверный пароль")
        return value

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save(update_fields=["is_active"])
        return instance


class UserShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("id", "email", "first_name", "last_name", "role")


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ("password", "new_password", "repeat_password")

    def validate(self, data):
        password = data.get("password")
        new_password = data.get("new_password")
        repeat_password = data.get("repeat_password")
        if new_password != repeat_password:
            raise ValidationError("Введите дважды одинаковый пароль")
        try:
            validate_password(new_password)
        except ValidationError as e:
            raise serializers.ValidationError(
                {"Пароль не соответствует требования безопасности": list(e.messages)}
            )
        user = self.instance
        if not user.check_password(password):
            raise serializers.ValidationError("Неверный пароль")
        return data
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("new_password"))
        instance.save()
        return instance

