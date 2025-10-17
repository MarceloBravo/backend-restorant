from django_filters import rest_framework as filters
from products.models import Product

class ProductFilter(filters.FilterSet):
    """
    Filtro personalizado para los productos.
    """
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'active': ['exact'],
            'price': ['exact', 'gte', 'lte'], # gte (>=), lte (<=)
        }