# views.py

from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('productName')
    serializer_class = ProductSerializer
