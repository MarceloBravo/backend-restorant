from django.contrib import admin
from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','description','price','active','category','image', 'created_at','updated_at']
    search_fields=['title','description','price','active','category']
    list_filter=['created_at','updated_at']