# views.py

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
import datetime

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('productName')
    serializer_class = ProductSerializer

