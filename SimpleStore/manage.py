#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from store.models import Product
newProduct = Product()
newProdcut.name = "Keyboard"
newProduct.price = 14.99
newProduct.description = "PC Keyboard"
newProduct.imglink = "C:\Users\hp\Desktop\NAJIA.jpg"
newProduct.save()
Product.objects.all()

newProduct_1.name = "PC Mouse"
newProduct_1.description = "A Device for PC User"
newProduct_1.imglink = "https://image.shutterstock.com/image-photo/closeup-nature-view-green-leaf-600w-387062149.jpg"
newProduct_1.save()



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleStore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
