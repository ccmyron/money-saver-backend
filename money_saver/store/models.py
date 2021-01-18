from django.db import models
from django.conf import settings


class Product(models.Model):
    productName = models.CharField(max_length=255)    # Name of the product
    productPrice = models.CharField(max_length=7)     # Price of the product
    productLink = models.CharField(max_length=255)    # Link to the product
    productImg = models.CharField(max_length=255)     # Link to the product image

    def __str__(self):
        return self.productName
