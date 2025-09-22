from rest_framework.serializers import Serializer
from categories.models import Category

class CategorySerializer(Serializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'image']