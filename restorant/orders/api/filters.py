from django_filters import rest_framework as filters
from orders.models import Order

class OrderFilter(filters.FilterSet):
    """
    Filtro personalizado para los productos.
    """
    class Meta:
        model = Order
        fields = {
            'table': ['exact'],
            'pending': ['exact'],
            'close': ['exact'],
            'total': ['exact', 'gte', 'lte'], # gte (>=), lte (<=)
        }