from django.contrib import admin

# Register your models here.
from tables.models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'active', 'created_at', 'updated_at')
    search_fields = ('number', 'capacity', 'active')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')