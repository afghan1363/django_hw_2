# Generated by Django 4.2.6 on 2023-11-21 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category',), 'permissions': [('set_published', 'Can published for sale')], 'verbose_name': 'Приложение', 'verbose_name_plural': 'Приложения'},
        ),
    ]
