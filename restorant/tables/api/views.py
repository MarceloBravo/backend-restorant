from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from tables.models import Table
from tables.api.serializers import TableSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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