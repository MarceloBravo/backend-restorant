from rest_framework.routers import DefaultRouter
from orders.api.views import OrderViewSet

router_order = DefaultRouter()

router_order.register(
    prefix="orders",
    viewset=OrderViewSet,
    basename="orders"
)