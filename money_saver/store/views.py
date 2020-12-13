# store/views.py

from django.shortcuts import render
from django.http import HttpResponse
import json


def homepage(request):
    return render(request, 'store/index.html')

def productDetail(request):
    return render(request, 'store/product-detail.html')

def aboutPage(request):
    return render(request, 'store/about.html')    

def contactPage(request):
    return render(request, 'store/contact.html')


def parsejson(request):
    with open('../scraper_data/Products_Pandashop.json') as pandashop:
        data = json.load(pandashop)

    print(data)    

    return render(request, 'store/home.html')

