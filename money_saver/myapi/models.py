# models.py

from django.db import models

class Product(models.Model):
    productShop = models.CharField(max_length=20)    # Shop, where we take the price
    productName = models.CharField(max_length=30)    # Name of the product
    productPrice = models.FloatField()               # Price of the product

    def __str__(self):
        return self.productName
