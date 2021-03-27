import requests
import lxml
import urllib.request
import urllib3
import shutil
import tempfile
import html5lib
import csv
import math
import pandas as pd
import pandas
from bs4 import BeautifulSoup
import re
# with result code 200, means http code is succesfully processed and net is working fine.
webUrl = urllib.request.urlopen("https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwa")
print("resultcode: " + str(webUrl.getcode()))
input("Hello, what you would like to buy from your standard list?")
from test import product_details
product_details()
from test import dict_
dict_()

'''from test import #aashirwaad_aata, #hello, product_details #aa_aata
 #aashirwaad_aata("www.bigbasket.com",5)
 #aashirwaad_aata("www.jiomart.com",5)
 #aashirwaad_aata("www.flipkart.com",5)'''
product_details()
 #aa_aata()




'''reader = csv.reader("C:\\Users\\Sudheerk\\PycharmProjects\\sahi-keemat\\Grocery_url_list1.csv")
with open("C:\\Users\\Sudheerk\\PycharmProjects\\sahi-keemat\\Grocery_url_list1.csv", newline='' ) as File:
    reader = csv.reader(File)
    for row in reader:
     print(row[2], row[3])'''



#hello()
#hello("https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwa")
#hello("https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'")
#hello("https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace")
#aashirwaad_aata('www.bigbasket.com', 5)
#aashirwaad_aata('www.jiomart.com', 5)
#aashirwaad_aata('www.flipkart.com', 5)
#extract_url("www.bigbasket.com")
#product_details()
#page = requests.get(url, headers= headers)
#soup = BeautifulSoup(page.content, "html5lib")
#title = soup.find(id="productTitle")
#price = soup.find(id="priceblock_dealprice")

#response = requests.get("https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwa")
#response.Class = ("tQ1Iy")
#print(response.content)
#from test import bb_aata
#bb_aata()
#f = open("test.py")
#print(bb_aata_url)

#def aashirwaad_aata(url):

#def jio_mart():
#def flip_kart():
#def convert_price_float():

