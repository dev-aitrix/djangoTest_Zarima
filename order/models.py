from django.db import models
from users.models import User
import uuid
from product.models import Product

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    sum_order = models.FloatField(default=0)


class ProductOrder(models.Model):
    id_order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    id_product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()