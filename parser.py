import urllib.request
import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://smilefood.od.ua/products/pizza'
response = requests.get(url)
contents = response.text
soup = BeautifulSoup(contents, 'lxml')

pizzas_data = []
products = soup.find_all('div', {'class': 'product'})

for product in products:
    pizza = {}
    images = product.find_all('div', {'class': 'product-img'})
    product_desc = product.find_all('div', {'class': 'product-desc'})
    for value in product_desc:
        product_top = value.find_all('div', {'class': 'product-top'})
        product_text = value.find_all('div', {'class': 'product-text'})
        product_bottom = value.find_all('div', {'class': 'product-bottom'})
        for product_name in product_top:
            names = value.find_all('a', {'class': 'product-name'})
            for name in names:
                if name.span.contents:
                    if name.span.contents[0]:
                        pizza['name'] = name.span.contents[0]
        for text in product_text:
            pizza['text'] = text.contents[0].replace('\r\n', '')
        for product_sum in product_bottom:
            prices = product_sum.find_all('div', {'class': 'product-sum'})
            for price in prices:
                pizza['price'] = price.span.contents[0]
        for image in images:
            pizza['image_url'] = image.img['src']
        if pizza not in pizzas_data:
            pizzas_data.append(pizza)

pprint(pizzas_data)
