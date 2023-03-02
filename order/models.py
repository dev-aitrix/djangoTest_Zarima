from django.db import models
from users.models import UserModel
import uuid
from product.models import ProductModel

# Create your models here.

class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(to=UserModel, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sum_order = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductInOrderModel(models.Model):
    id_order = models.ForeignKey(to=OrderModel, related_name='products', on_delete=models.CASCADE)
    id_product = models.ForeignKey(to=ProductModel,related_name='order', on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        verbose_name = 'Заказ в товаре'
        verbose_name_plural = 'Заказы в товарах'