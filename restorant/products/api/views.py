from rest_framework.viewsets import ModelViewSet
from products.models import Product
from products.api.serializers import ProductSerializer
from products.api.filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

class ProductViewSet(ModelViewSet ):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    # Se combinan dos backends: uno para filtros exactos y otro para búsqueda de texto.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Usamos nuestra clase de filtro personalizada
    filterset_class = ProductFilter
    # Campos para búsqueda por texto (ej: /api/products/?search=pizza)
    search_fields = ['title', 'description']

    @action(detail=False, methods=['post'], url_path='upload')
    def upload_image(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        path = os.path.join('products', image.name)
        saved_path = default_storage.save(path, ContentFile(image.read()))
        image_url = os.path.join(settings.MEDIA_URL, saved_path).replace('\\', '/')

        return Response({'image_path': image_url}, status=status.HTTP_201_CREATED)