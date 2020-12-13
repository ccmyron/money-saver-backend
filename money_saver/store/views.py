# store/views.py

from django.shortcuts import render
from django.http import HttpResponse

import json

def home(request):
    return render(request, 'store/home.html')


def parsejson(request):
    with open('../scraper_data/Products_Pandashop.json') as pandashop:
        data = json.load(pandashop)

    print(data)    

    return render(request, 'store/home.html')

