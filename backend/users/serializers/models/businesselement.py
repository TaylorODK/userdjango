from rest_framework import serializers
from users.models import BusinessElement


class BusinessElementSerializer(serializers.ModelSerializer):
    """Сериализатор бизнес-элементов."""

    class Meta:
        model = BusinessElement
        fields = ("id", "name", "slug", "description")
