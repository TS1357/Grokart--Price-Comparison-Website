import requests as req
from bs4 import BeautifulSoup


def sort_name(name):
    """ removes whitespace from product name"""
    name_list = name.split()
    sorted_name = " ".join(name_list)
    return sorted_name


def create_soup_page(url):
    webpage = req.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    return soup


def dmart_scrape(url):
    """returns the item price for a dmart product"""
    soup = create_soup_page(url)
    try:
        price_units = soup.find("span", class_="src-client-app-product-details-styles-__price-details-component-module___value").getText().strip()
        product_price = price_units.partition("")[1]
        if "p" in product_price:
            product_price_pence = product_price.replace("p", "")
            product_price_final = float(product_price_pence)/100
        else:
            product_price_final = price_units.partition("/")[0][1:]

        return product_price

    except AttributeError:
        print("Failed- investigate: {}".format(url))


def bigbasket_scrape(url):
    """returns the item price for a bigbasket product"""
    soup = create_soup_page(url)
    try:
        product_description = soup.find("div", class_="related-search-ribbon-enabled")

        try:
            product_price_raw = product_description.find(class_="nowPrice").getText()
            product_price = product_price_raw.strip()[1:]
        except AttributeError:
            # If the nowPrice isn't available it means the product is on offer.
            product_price_raw = product_description.find(class_="typicalPrice").getText()
            product_price = product_price_raw.strip()[1:]

        return product_price
    except AttributeError:
        print("Failed- investigate: {}".format(url))


def amazon_scrape(url):
    """returns the item price for a amazon product"""
    soup = create_soup_page(url)
    try:
        bs  = soup.find("span", class_ = "a-price-whole")
        if bs == None:
            bs = soup.find("span", class_ = "a-size-medium a-color-price")
            product_price = bs.get_text()[1:]
        else:
            product_price = bs.get_text()[:-1]
        
        return product_price

    except AttributeError:
        print("Failed- investigate: {}".format(url))
