from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryViewSet

router_category = DefaultRouter()

router_category.register(
    prefix="categories",
    viewset=CategoryViewSet,
    basename="categories"
)

