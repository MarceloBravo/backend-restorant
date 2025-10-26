from rest_framework.serializers import ModelSerializer
from tables.models import Table

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'capacity', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']