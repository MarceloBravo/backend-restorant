from rest_framework.serializers import ModelSerializer, SerializerMethodField
from tables.models import Table
from orders.models import Order


class SimpleTableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'capacity', 'active', 'created_at', 'updated_at']


class TableSerializer(SimpleTableSerializer):
    orders = SerializerMethodField()

    class Meta(SimpleTableSerializer.Meta):
        fields = SimpleTableSerializer.Meta.fields + ['orders']

    def get_orders(self, obj):
        from orders.api.serializers import OrderSerializer
        request = self.context.get('request')
        orders_queryset = obj.orders.all()

        if request:
            sort_by = request.query_params.get('sort_by')
            order = request.query_params.get('order', 'asc')

            if sort_by == 'status_created_at':
                # Sort by status (desc) and then by created_at (desc)
                orders_queryset = orders_queryset.order_by('-status', '-created_at')
            elif sort_by in ['status', 'created_at']:
                if order.lower() == 'desc':
                    sort_by = f'-{sort_by}'
                orders_queryset = orders_queryset.order_by(sort_by)
            
            serializer = OrderSerializer(orders_queryset, many=True)
            return serializer.data
        
        return OrderSerializer(orders_queryset, many=True).data