from rest_framework.routers import DefaultRouter
from tables.api.views import TableViewSet
from categories.api.views import CategoryViewSet

router_table = DefaultRouter()

router_table.register(
    prefix="tables",
    viewset=TableViewSet,
    basename="tables"
)