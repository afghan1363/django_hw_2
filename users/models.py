from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None  # для деактивации главного поля авторизации
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='Ава', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна')
    email = models.EmailField(unique=True, verbose_name='Почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
