from rest_framework.routers import DefaultRouter
from products.api.views import ProductViewSet

router_product = DefaultRouter()

router_product.register(
    prefix="products",
    viewset=ProductViewSet,
    basename="products"
)