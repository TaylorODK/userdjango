from rest_framework import serializers
from users.models import AccessRolesRule
from rest_framework.serializers import ValidationError


class AccessShowSerializer(serializers.ModelSerializer):
    """Сериализатор отображения уровня доступа текущего пользователя."""
    role = serializers.StringRelatedField()
    element = serializers.StringRelatedField()
    rules = serializers.SerializerMethodField()

    class Meta:
        model = AccessRolesRule
        fields = ("role", "element", "rules")

    def get_rules(self, instance):
        access = instance
        return {
            "Доступ для чтения собственного объекта модели": access.read_permission,
            "Доступ для чтения всех объектов модели": access.read_all_permission,
            "Доступ для создания объекта модели": access.create_permission,
            "Возможность редактирования собственного объекта модели": access.update_permission,
            "Возможность редактирования всех объектов модели": access.update_all_permission,
            "Возможность удаления собственного объекта модели": access.delete_permission,
            "Возможность удаления всех объектов модели": access.delete_all_permission,
        }


class AccessChangeSerializer(serializers.ModelSerializer):
    pass
