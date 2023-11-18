from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None  # для деактивации главного поля авторизации
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    is_active = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=4, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
