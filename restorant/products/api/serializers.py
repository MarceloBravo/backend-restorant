from rest_framework.serializers import ModelSerializer, CharField
from products.models import Product

class ProductSerializer(ModelSerializer):
    category_name = CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category', 'category_name', 'image', 'created_at', 'updated_at']