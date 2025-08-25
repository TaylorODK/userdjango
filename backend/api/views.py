from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from drf_spectacular.utils import extend_schema
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer
from .permissions import AuthorPermission
from .schemas import (
    order_content_schema,
    product_content_schema,
    product_create_schema,
    order_create_schema,
)

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = (AuthorPermission,)
    serializer_class = OrderSerializer

    @order_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @order_content_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


@product_content_schema
class ProductListViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer


class ProductViewSet(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"

    def get_permissions(self):
        if self.action == "retrieve":
            return [
                IsAuthenticated,
            ]
        return [
            IsAdminUser,
        ]

    @product_content_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @product_create_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
