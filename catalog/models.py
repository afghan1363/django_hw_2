from django.db import models

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
    image = models.ImageField(upload_to='students/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_create = models.DateField(verbose_name='Дата создания')
    date_of_change = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)
