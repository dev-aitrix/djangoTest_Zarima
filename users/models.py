from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    email = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=6)
    address = models.TextField(default=0)
    number_phone = models.CharField(max_length=10)


    def __str__(self):
        return self.name