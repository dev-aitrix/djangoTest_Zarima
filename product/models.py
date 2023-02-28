from django.db import models
import uuid


# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField()


    def __str__(self):
        return self.name

