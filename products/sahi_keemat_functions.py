import csv
# from csv import reader,DictReader,DictWriter,writer
from operator import itemgetter
import math
import regex
import re
import requests
from bs4 import BeautifulSoup
import os




def get_converted_price(price):
 stripped_price = price.strip("Rs ,")
 replaced_price = stripped_price.replace(",", "")
 find_dot = replaced_price.find(".")
 to_convert_price = replaced_price[0:find_dot]
 # converted_price = int(to_convert_price)
 converted_price = float(re.sub(r"[^\d.]", "", price))
 return converted_price


def bb_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 bb_product = soup.find(class_="_2j_7u")
 soup.span = soup.find('span', class_="_2j_7u")
  bb_product_price = (soup.span.text)
  bb_price = get_converted_price(bb_product_price)
  return bb_price



def jio_get_price(url):
 headers = {
  "User-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

 page = requests.get(url)
 soup = BeautifulSoup(page.text, 'html.parser')
 jio_product_price = soup.find(class_="final-price")
 soup.span = soup.find('span', class_="final-price")
 jio_product_price = (soup.span.text)
 jio_price = get_converted_price(jio_product_price)
 return jio_price




def new_csv(file_path):

 fieldnames = ['site_name', 'url']
 with open(file_path, "w") as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()

 return


def get_length(file_path):
 return file_path


def append_data(file_path, source, price):
 fieldnames = ['url', 'price']
 with open(file_path, 'a') as csvfile:
  writer = csv.DictWriter((csvfile), fieldnames=fieldnames)
  writer.writerow({
   "url": source,
   "price": price
  })

 return


def product_value(file):  # getting the value(url) for the key(product) and passing it in the price functions

 reader = csv.reader(open(file, 'r'))

 product_list = {}
 for row in reader:
  k, v = row
  product_list[k] = v
 #print(product_list)

 key = list(product_list.keys())[0]  # getting the key by passing the index
 
 #print("The 1st key of dictionary is : " + str(key))
 
 a1 = product_list['bigbasket']
 bb_price = bb_get_price(a1)
 #print(product_list['bigbasket'] + ":" + str(bb_price))

 
 a2 = product_list['jiomart']
 jio_price = jio_get_price(a2)
 #print(product_list['jiomart'] + ":" + str(jio_price))

 test_dict = {list(product_list.keys())[0]: (a1, str(bb_price)), list(product_list.keys())[1]: (a2, str(jio_price))}
 #print(test_dict)
 Table = []
 for key, value in test_dict.items():  # or .items() in Python 3
  temp = []
  temp.extend([key, value])  # Note that this will change depending on the structure of your dictionary
  Table.append(temp)

 
def product_details():
 path = "csv_files\\"
 items = os.listdir(path)
 products_data = {}

 for file in items:

  product_info= product_value(path+file)
  products_data[file] = product_info
     
 return products_data


