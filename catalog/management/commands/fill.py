import json
from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Cleaning table Category
        Category.objects.all().delete()

        # Clearing autoincrement for pk filed table Category
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        # Fill file
        category_for_create = [
            {'name':'Vegetables', 'description': 'Local Vegetables'},
            {'name':'Fruits', 'description': 'Local Fruits'},
            {'name':'Products for babies', 'description': 'Products for children age up to 3 y.o '},
            {'name':'Meat', 'description': 'Beef, chicken, fish, turkey'},
            {'name':'Bakery', 'description': 'buns, pies, donuts and so on'}
        ]
        for category_item in category_for_create:
            Category.objects.create(**category_item)
