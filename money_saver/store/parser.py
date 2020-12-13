from .models import Product
import json

if __name__ == "__main__":

    # with open('../Money Saver/scraper_data/Products_Pandashop.json') as pandashop:
    #     pandaShopData = json.load(pandashop)

    # with open('../Money Saver/scraper_data/Products_Cactus.json', encoding='UTF-8') as cactus:
    #     cactusData = json.load(cactus)

    # with open('../Money Saver/scraper_data/Products_Rozetka.json', encoding='UTF-8') as rozetka:
    #     rozetkaData = json.load(rozetka)

    # test json
    with open('Products_Pandashop.json') as pandashop:
        pandaShopData = json.load(pandashop)

    with open('Products_Cactus.json', encoding='UTF-8') as cactus:
        cactusData = json.load(cactus)

    with open('Products_Rozetka.json', encoding='UTF-8') as rozetka:
        rozetkaData = json.load(rozetka)

    data = pandaShopData
    data.update(cactusData)
    data.update(rozetkaData)
    
    import sqlite3
    db = sqlite3.connect('db.sqlite3')

    for shop in data:
        for prod in range(len(data[shop])):
            # print(data[shop][prod]['name'])
            #p = Product(productShop=data[shop]['shop'], productName=data[shop]['name'])  
            


    #TODO: parse out the info to the db
