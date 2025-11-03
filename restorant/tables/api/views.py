from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from tables.models import Table
from tables.api.serializers import TableSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TableViewSet(ModelViewSet):
    queryset = Table.objects.prefetch_related('orders').all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TableSerializer

    # Habilitar el backend de búsqueda
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['number', 'capacity', 'active']
    search_fields = ['number', 'capacity', 'active']
    ordering_fields = ['number', 'capacity']
    ordering = ['number']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'sort_by',
                openapi.IN_QUERY,
                description="Sort orders by 'status', 'created_at', or 'status_created_at'",
                type=openapi.TYPE_STRING,
                enum=['status', 'created_at', 'status_created_at']
            ),
            openapi.Parameter(
                'order',
                openapi.IN_QUERY,
                description="Order 'asc' or 'desc'",
                type=openapi.TYPE_STRING,
                enum=['asc', 'desc']
            ),
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)