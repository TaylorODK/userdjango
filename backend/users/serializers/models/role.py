from rest_framework import serializers
from users.models import Role


class RoleSerializer(serializers.ModelSerializer):
    """Сериализатор предоставления инфомации по ролям."""

    class Meta:
        model = Role
        fields = ("id", "name", "slug", "description")
