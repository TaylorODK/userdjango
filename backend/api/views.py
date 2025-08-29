from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
)
from drf_spectacular.utils import extend_schema_view
from api.models import Order, Product
from api.permissions import AccessPermission

from api.serializers import OrderSerializer, ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AccessPermission,)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AccessPermission,)
    lookup_field = "id"
