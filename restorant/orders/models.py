from django.db import models

# Create your models here.
class Order(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True, blank=True)
    pending = models.BooleanField(default=True)
    close = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.id}"

