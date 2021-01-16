from bs4 import BeautifulSoup as soup
import requests
import os

wordFilterList = [
    'Telefon', 'Mobil',
    'Black', 'Leather', 'Jet', 'Prism', 'Light', 'Onyx', 'Crush',
    'White', 'Prism', 'Polar',
    'Blue', 'Pacific', 'Crystal', 'Ice',
    'Red',
    'Green', 'Forest', 'Tropical', 'Verde',
    'Orange',
    'Pink', 'Cloud',
    'Purple', 'Nebula',
    'Silver',
    'Yellow',
    'Gold',
    'Pacific Blue',
    'Rose Gold',
    'Gray', 'Grey', 'Cosmic', 'Glacier', 'Space',
    'Sorta Sage',
    'Brown',
    'Titan',
    'Graphite',
    'Cloud', 'Navy',
    'Mint'
]

def scrapeSmart():

    # filename = 'productssmart.csv'
    # f = open(filename, 'w')
    # headers = "Name, Price, Link, Img\n"
    # f.write(headers)

    productInfo = []
    currentPage = 1
    
    while True:
   
        siteURL = 'https://www.smart.md/smartphone?page='+format(currentPage)

        # grab the html document
        pageData = requests.get(siteURL)

        # parse the html document
        pageSoup = soup(pageData.content, "html.parser")

        # grab product containers
        containerAttribute = {"class" : "col m4 s6 pre_bloc_prod_cont row_special"}
        containers = pageSoup.findAll("div", containerAttribute)

        # loop through the containers and parse out the data:
        for container in containers:
            
            # grab the product name
            productName = container.div.a['title']
            productNameWords = productName.split()
            resultWords = [word for word in productNameWords if word not in wordFilterList]
            productName = ' '.join(resultWords).replace(',', '')

            # find the price container, and parse the price
            priceAttribute = {"class" : "price_prod"}
            priceContainer = container.div.find(attrs=priceAttribute)
            productPrice = priceContainer.span.text.replace(' lei', '')
            productPrice = productPrice.translate({ord(i): None for i in ' \n'})

            # grab the product link
            productLink = container.div.a['href']

            # grab the link to the photo
            productImg = container.div.a.img['data-src']

            # form a tuple from this info and dump it into the list
            productTuple = (productName, productPrice, productLink, productImg)
            productInfo.append(productTuple)

            # f.write(productName + ',' + productPrice + ',' + productLink + ',' + productImg + '\n')


        stopSignal = {'class' : 'disabled last_desktop _desktop'}
        if pageSoup.find("li", attrs=stopSignal):
            break

        currentPage+=1
# end of the function scrapeSmart()


def scrapeDarwin():

    # filename = 'productsdarwin.csv'
    # f = open(filename, 'w')
    # headers = "Name, Price, Link, Img\n"
    # f.write(headers)


    productInfo = []
    currentPage = 1

    for index in range(30):

        siteURL = 'https://darwin.md/telefoane/smartphone?page='+format(index)
        
        # grab the html document
        pageData = requests.get(siteURL)

        # parse the html document
        pageSoup = soup(pageData.content, "html.parser")

        # grab product containers
        containerAttribute = {"class" : "col-6 col-md-4 col-lg-3"}
        containers = pageSoup.findAll("div", containerAttribute)

        # loop through the containers and parse out the data:
        for container in containers:

            # grab the product name
            productName = container.figure.figcaption.h3.a.text
            productNameWords = productName.split()
            resultWords = [word for word in productNameWords if word not in wordFilterList]
            productName = ' '.join(resultWords).replace(',', '')

            # find the price container, and parse the price
            priceAttribute = {"class" : "price-new"}
            priceContainer = container.figure.find(attrs=priceAttribute)
            productPrice = priceContainer.text.replace(' lei', '')
            productPrice = productPrice.translate({ord(i): None for i in ' \n'})

            # grab the product link
            productLinkAttribute = {"class" : "img-wrap"}
            productLinkContainer = container.figure.find(attrs=productLinkAttribute)
            productLink = productLinkContainer.a['href']

            # grab the link to the photo
            productImg = productLinkContainer.img['src']
            
            # form a tuple from this info and dump it into the list
            productTuple = (productName, productPrice, productLink, productImg)
            productInfo.append(productTuple)
            # f.write(productName + ',' + productPrice + ',' + productLink + ',' + productImg + '\n')
# end of the function scrapeDarwin()

def scrapeGsmShop():

    productInfo = []
    currentPage = 1
    
    while True:
   
        siteURL = 'https://www.gsmshop.md/category/view/mobile-phones/'+format(currentPage)+'html'

        # grab the html document
        pageData = requests.get(siteURL)

        # parse the html document
        pageSoup = soup(pageData.content, "html.parser")

        # grab product containers
        containerAttribute = {"class" : "phone_bls wide notranslate"}
        containers = pageSoup.findAll("div", containerAttribute)
        print(containers[0])

# end of the function scrapeGsmShop

#TODO complete scraper for orange
def scrapeOrange():
    pass


if __name__ == '__main__':
    scrapeGsmShop()

