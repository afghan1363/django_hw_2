import os

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка таблицы Product
        Product.objects.all().delete()

        # Очистка таблицы Category
        Category.objects.all().delete()
        # Сброс автоинкремента для поля `pk` в таблице Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Сброс автоинкремента для поля `pk` в таблице Product
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")
        # return os.system("python manage.py loaddata catalog.json")
