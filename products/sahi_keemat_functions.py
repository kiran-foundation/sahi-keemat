import csv
from csv import reader,DictReader,DictWriter,writer
from operator import itemgetter
import re
import requests
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
 #price = bb_get_price('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad')
 bb_price = get_converted_price(bb_product_price)
 return bb_price

'''
URL = 'https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad'
price = bb_get_price(URL)
bb_price = get_converted_price(price)
print(bb_price)
'''

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

'''URL = 'https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'
price1 = jio_get_price(URL)
jio_price = get_converted_price(price1)
print(jio_price)
'''
def flip_kart_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 fk_product_price = soup.find(class_="_30jeq3 _16Jk6d")

 fk_product_price = soup.find("div",{'class': "_30jeq3 _16Jk6d"}).decompose()
# fk_product_price = (soup.div.text)
 fk_price = get_converted_price(fk_product_price)
 return fk_price

'''
URL = 'https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-299fcdeed8eb.FLREUC5PSFQUBHTC.SEARCH'
price2 = flip_kart_get_price(URL)
print(price2)# rs235 not displaying
'''

def new_csv(file_path):
 #'product_name',
 fieldnames = ['source', 'price']
 with open(file_path ,"w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

 return


def get_length(file_path):
 return file_path

def append_data(file_path,source,price):
 #'product_name',
 fieldnames = ['source', 'price']
 #next_name = get_length(file_path)

 with open(file_path, 'a') as csvfile:
     writer = csv.DictWriter(csvfile,fieldnames= fieldnames)
     #writer.writeheader()
     writer.writerow({
  #    "product_name": next_name,
      "source": source,
      "price":  price
     })
