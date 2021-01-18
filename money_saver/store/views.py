# store/views.py

from django.shortcuts import render
from django.http import HttpResponse
from scripts.bs4scraper import scrapeDriver
import sqlite3


def homepage(request):
    return render(request, 'store/index.html')

def productDetail(request):
    return render(request, 'store/product-detail.html')

def aboutPage(request):
    return render(request, 'store/about.html')    

def contactPage(request):
    return render(request, 'store/contact.html')

def serializeModels(request):

    # connect to the database
    conn = sqlite3.connect('../db.sqlite3')

    # create the cursor
    curs = conn.cursor()

    # execute the script and store all the scraped data into a list
    productList = scrapeDriver()

    # create a table products
    curs.execute("""CREATE TABLE products(
            productName text,
            productPrice text,
            productLink text,
            productImg text
    )""")

    # commit the table creation
    conn.commit()

    # insert the data from the list
    curs.executemany("INSERT INTO products VALUES (?,?,?,?)", productList)

    # commit and close the connection
    conn.commit()
    conn.close()

    return render(request, 'store/home.html')

