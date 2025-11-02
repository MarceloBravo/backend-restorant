from django_filters import rest_framework as filters
from orders.models import Order


class OrderFilter(filters.FilterSet):
    """FilterSet para Order con filtros explícitos."""
    table = filters.NumberFilter(field_name='table', lookup_expr='exact')
    status = filters.ChoiceFilter(field_name='status', choices=Order.Status.choices)
    total_min = filters.NumberFilter(field_name='total', lookup_expr='gte')
    total_max = filters.NumberFilter(field_name='total', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['table', 'status', 'total']