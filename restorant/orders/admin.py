from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'products', 'status', 'quantity', 'total', 'created_at', 'updated_at')
    list_filter = ('table', 'products', 'status', 'total', 'created_at', 'updated_at')
    search_fields = ('id','table', 'products', 'status')
    ordering = ('-created_at','table', 'status')

admin.site.register(Order, OrderAdmin)