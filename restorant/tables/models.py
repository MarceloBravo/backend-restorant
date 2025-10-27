from django.db import models

# Create your models here.
class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"