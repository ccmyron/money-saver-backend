from bs4 import BeautifulSoup as soup
import requests
import os

wordFilterList = [
    'Telefon', 'Mobil',
    'Мобильный', 'телефон',
    'Black', 'Leather', 'Jet', 'Prism', 'Light', 'Onyx', 'Crush',
    'White', 'Prism', 'Polar', 'Pearl',
    'Blue', 'Pacific', 'Crystal', 'Ice', 'Ocean', 'Starscape',
    'Peacock', 'Sky',
    'Red',
    'Green', 'Forest', 'Tropical', 'Verde',
    'Orange',
    'Pink', 'Cloud',
    'Purple', 'Nebula',
    'Silver', 'Dark',
    'Yellow',
    'Gold',
    'Pacific Blue',
    'Rose Gold',
    'Gray', 'Grey', 'Cosmic', 'Glacier', 'Space', 'Interstellar',
    'Moonshadow', 'Mineral', 'Carbon',
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

    return productInfo
# end of the function scrapeSmart()


def scrapeDarwin():

    # filename = 'productsdarwin.csv'
    # f = open(filename, 'w')
    # headers = "Name, Price, Link, Img\n"
    # f.write(headers)


    productInfo = []
    # currentPage = 1

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


    return productInfo
# end of the function scrapeDarwin()

def scrapeGsmShop():

    # filename = 'productsgsmshop.csv'
    # f = open(filename, 'w')
    # headers = "Name, Price, Link, Img\n"
    # f.write(headers)

    productInfo = []
    currentPage = 1
    scriptActive = True
    
    while scriptActive:
   
        siteURL = 'https://www.gsmshop.md/category/view/mobile-phones/'+format(currentPage)+'.html'

        # grab the html document
        pageData = requests.get(siteURL)

        # parse the html document
        pageSoup = soup(pageData.content, "html.parser")

        # grab product containers
        containerAttribute = {"class" : "phone_bls wide notranslate"}
        containers = pageSoup.findAll("div", containerAttribute)

        for container in containers:
            
            # Check if there is need to continue parsing
            stopSignal = {'class' : 'phone_bls_notaval'}
            if container.find(attrs=stopSignal):
                scriptActive = False
                break

            # grab the product name
            productName = container.div.a.h2.text
            productNameWords = productName.split()
            resultWords = [word for word in productNameWords if word not in wordFilterList]
            productName = ' '.join(resultWords).replace(',', '')

            # find the price container, and parse the price
            priceAttribute = {"class" : "phone_bls_price notranslate"}
            priceContainer = container.find(attrs=priceAttribute)
            productPrice = priceContainer.text.replace('MDL', '')
            productPrice = productPrice.translate({ord(i): None for i in ' \n'})

            # grab the product link
            productLink = 'https://www.gsmshop.md' + container.div.a['href']

            # grab the link to the photo
            productImgContainerAttribute = {"class" : "phone_bls_img"}
            productImgContainer = container.find(attrs=productImgContainerAttribute)
            productImg = 'https://www.gsmshop.md' + productImgContainer.div.a.img['src']

            # form a tuple from this info and dump it into the list
            productTuple = (productName, productPrice, productLink, productImg)
            productInfo.append(productTuple)

            # f.write(productName + ',' + productPrice + ',' + productLink + ',' + productImg + '\n')

        #print(f'{currentPage} pages scraped')
        currentPage+=1
    
    return productInfo
# end of the function scrapeGsmShop()

def scrapePandashop():

    # filename = 'productspandashop.csv'
    # f = open(filename, 'w')
    # headers = "Name, Price, Link, Img\n"
    # f.write(headers)


    productInfo = []
    currentPage = 1
    scriptActive = True

    while scriptActive:

        siteURL = 'https://www.pandashop.md/ru/catalog/electronics/telephones/mobile/?page_=page_'+format(currentPage)
        
        # grab the html document
        pageData = requests.get(siteURL)

        # parse the html document
        pageSoup = soup(pageData.content, "html.parser")
        
        # grab containers
        containerAttribute = {"class" : "card js-itemsList-item"}
        containers = pageSoup.findAll(attrs=containerAttribute)

        for container in containers:
            
            # grab the product name
            productNameContainer = container.find('div', {'class' : 'card-inner'})
            productName = productNameContainer.a.div.picture.img['alt']
            productNameWords = productName.split()
            resultWords = [word for word in productNameWords if word not in wordFilterList]
            productName = ' '.join(resultWords).replace(',', '')

            # find the price container, and parse the price
            priceAttribute = {"class" : "card-footer"}
            priceContainer = container.find(attrs=priceAttribute)
            productPrice = priceContainer.div.div.span.text.replace('лей', '')
            productPrice = productPrice.translate({ord(i): None for i in ' \n'})
            if '%' in productPrice:
                continue

            # grab the product link
            productLink = 'https://www.pandashop.md' + container.a['href']

            # grab the link to the photo
            productImg = container.a.div.picture.img['data-src']

            # form a tuple from this info and dump it into the list
            productTuple = (productName, productPrice, productLink, productImg)
            productInfo.append(productTuple)

            #f.write(productName + ',' + productPrice + ',' + productLink + ',' + productImg + '\n')

        stopSignal = {'class' : 'btn btn-orange btn-showmore'}
        if not pageSoup.find(attrs=stopSignal):
            scriptActive = False

        currentPage+=1
    
    return productInfo
# end of the function scrapeOrange()    

def scrapeDriver():

    productInfoFinal = scrapeDarwin()
    productInfoFinal += scrapeGsmShop()
    productInfoFinal += scrapePandashop()
    productInfoFinal += scrapeSmart()

    return productInfoFinal    
# end of the function scrapeDriver()
