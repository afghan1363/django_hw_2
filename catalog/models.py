from typing import Optional

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    date_of_create = models.DateField(verbose_name='Дата создания')
    date_of_change = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'''{self.title}:
{self.description}'''

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'
        ordering = ('category',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    title = models.CharField(max_length=150, verbose_name='Название версии', **NULLABLE)
    is_current = models.BooleanField(default=False, verbose_name='Активная')

    def __str__(self):
        return f'''{self.product}, 
версия: {self.version_number} {self.title}'''

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('product', 'title',)


# @receiver(post_save, sender=Version)
# def set_active_version(sender, instance, **kwargs):
#     if instance.is_active:
#         Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_active=False)
