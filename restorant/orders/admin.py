from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'products', 'pending', 'close', 'quantity', 'total', 'created_at', 'updated_at')
    list_filter = ('table', 'products', 'pending', 'close', 'total', 'created_at', 'updated_at')
    search_fields = ('id','table', 'products', 'pending', 'close',)
    ordering = ('-created_at','table', 'pending', 'close')

admin.site.register(Order, OrderAdmin)