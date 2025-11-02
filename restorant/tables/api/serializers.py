from rest_framework.serializers import ModelSerializer
from tables.models import Table
from orders.models import Order
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image']
        ref_name = 'TableProduct' 


class OrderSerializer(ModelSerializer):
    products = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'status', 'quantity','total', 'created_at', 'products']
        ref_name = 'NestedOrder'


class TableSerializer(ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ['id', 'number', 'capacity', 'active', 'orders', 'created_at', 'updated_at']