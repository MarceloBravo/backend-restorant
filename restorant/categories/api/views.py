from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    
    # Habilitar el backend de búsqueda
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=False, methods=['post'], url_path='upload')
    def upload_image(self, request):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

        path = os.path.join('categories', image.name)
        saved_path = default_storage.save(path, ContentFile(image.read()))
        image_url = os.path.join(settings.MEDIA_URL, saved_path).replace('\\', '/')

        return Response({'image_path': image_url}, status=status.HTTP_201_CREATED)