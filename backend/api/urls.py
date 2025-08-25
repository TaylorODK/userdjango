from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"order", OrderViewSet)
router.register(r"product", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
