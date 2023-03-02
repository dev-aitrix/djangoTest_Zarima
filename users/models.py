from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    number_phone = models.CharField(max_length=15)
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'