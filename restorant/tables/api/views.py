from rest_framework.viewsets import ModelViewSet
from tables.models import Table
from tables.api.serializers import TableSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TableSerializer

    # Habilitar el backend de búsqueda
    filterset_fields = ['number', 'capacity']
    search_fields = ['number', 'capacity']
    ordering_fields = ['number', 'capacity']
    ordering = ['number']