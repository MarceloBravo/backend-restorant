from rest_framework.serializers import ModelSerializer
from orders.models import Order

from products.api.serializers import ProductSerializer
from tables.api.serializers import SimpleTableSerializer

class OrderSerializer(ModelSerializer):
    product_data = ProductSerializer(source='products', read_only=True)
    table_data = SimpleTableSerializer(source='table', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'table_data', 'products', 'product_data', 'status', 'quantity', 'total', 'created_at', 'updated_at']
