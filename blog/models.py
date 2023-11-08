from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    slug = models.CharField(max_length=600, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='Содержимое')
    img_preview = models.ImageField(upload_to='blog_images/', verbose_name='Изображение-превью', **NULLABLE)
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'''{self.title}
{self.text[:100]}
{self.img_preview}'''

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('creation_date',)
