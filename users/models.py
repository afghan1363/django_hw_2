from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=35, verbose_name='Телефон')
    avatar = models.ImageField(upload_to='users/', verbose_name='Ава', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна')

