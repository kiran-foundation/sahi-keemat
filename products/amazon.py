
import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

URL = 'https://www.amazon.in/dp/B07S63PKXJ?ref_=Oct_DLandingS_D_dc7bc418_NA'

def amazon_de():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="a-size-small a-color-base")
    price = soup.find(class_="p13n-sc-price")
    sep = ','
    con_price = price.split(sep, 1)[0]
    converted_price = int(con_price.replace('.', ''))
    return converted_price

    # price
    price = amazon_de()
    print("p", price)
    print(title.strip())
    print(converted_price)

    price = bb_get_price(URL)
    bb_price = get_converted_price(price)
    print(bb_price)
