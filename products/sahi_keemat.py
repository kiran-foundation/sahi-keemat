from csv import reader,DictReader,DictWriter,writer
from operator import itemgetter
import re
import requests
import csv
from bs4 import BeautifulSoup


def get_converted_price(price):
 stripped_price = price.strip("Rs ,")
 replaced_price = stripped_price.replace("," , "")
 find_dot = replaced_price.find(".")
 to_convert_price = replaced_price[0:find_dot]
 # converted_price = int(to_convert_price)
 converted_price = float(re.sub(r"[^\d.]" , "" , price))
 return converted_price

def bb_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 bb_product = soup.find(class_="_2j_7u")
 soup.span = soup.find('span', class_="_2j_7u")
 #print(soup.span.text)
 bb_product_price = (soup.span.text)
 #price = bb_get_price('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashir

 bb_product_price = (soup.span.text)
 # price = bb_get_price('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad')
 bb_price = get_converted_price(bb_product_price)
 return bb_price

def jio_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 jio_product_price = soup.find(class_="final-price")
 soup.span = soup.find('span' , class_="final-price")
 jio_product_price = (soup.span.text)
 #print(jio_product_price)
 jio_price = get_converted_price(jio_product_price)
 return jio_price

def flip_kart_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 fk_product_price = soup.find(class_="_30jeq3 _16Jk6d")

 fk_product_price = soup.find("div", {'class': "_30jeq3 _16Jk6d"}).decompose()
     # fk_product_price = (soup.div.text)
 fk_price = get_converted_price(fk_product_price)
 return fk_price

def new_csv(file_path):
 fieldnames = ['product_name', 'source', 'price']
 with open(file_path ,"w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

 return