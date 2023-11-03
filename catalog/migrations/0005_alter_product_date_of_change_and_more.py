# Generated by Django 4.2.6 on 2023-10-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_create',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена за покупку'),
        ),
    ]