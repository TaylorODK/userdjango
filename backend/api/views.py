from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from drf_spectacular.utils import extend_schema
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .schemas import (
    order_content_schema,
    product_content_schema,
    product_create_schema,
    order_create_schema,
)

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @order_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @order_content_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProductViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == "create":
            return [
                IsAdminUser(),
            ]
        return [
            AllowAny(),
        ]

    @product_content_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @product_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @product_content_schema
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)