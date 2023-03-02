from django.db import models
import uuid


# Create your models here.

class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



