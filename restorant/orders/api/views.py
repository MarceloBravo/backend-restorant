from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from orders.models import Order
from orders.api.serializers import OrderSerializer
from orders.api.filters import OrderFilter

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # Use a FilterSet class for complex/custom filtering (defined in filters.py).
    # `filterset_class` expects a FilterSet class, while `filterset_fields` is
    # a shorthand to provide simple field names. We prefer using the FilterSet
    # for maintainability.
    filterset_class = OrderFilter

    # Allow ordering on all model fields (or set a tuple/list of allowed fields).
    ordering_fields = '__all__'

    # Combine filter backends: DjangoFilterBackend handles field filters;
    # OrderingFilter handles ordering via the `ordering` query param.
    filter_backends = [DjangoFilterBackend, OrderingFilter]