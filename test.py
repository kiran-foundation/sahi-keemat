import http
import csv
from _csv import reader
from csv import DictReader
import os

import requests
import re
from bs4 import BeautifulSoup #aashirwaad_aata
import re
import urllib
import shutil


#from functions_sk import webUrl
'''def print_lists():
    with open('C:\\Users\\Sudheerk\\PycharmProjects\\sahi-keemat\\Grocery3_url_list.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)

        row_number = 2
        col_number = 5
        value = list_of_rows[row_number - 1][col_number - 1]
        print('Value in cell at 3rd row and 5th column : ', value)'''
def test():
    with open('Grocery3_url_list.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        products = dict()
        for item in list_of_dict:
            products[item['p_id']] = item

        print(products['aa_1'])
test()
print(os.listdir('/Users/anurag/PycharmProjects/sahi-keemat'))

def read_product_csv(filename):
    return "dict_of_site_url"

def get_bigbasket_price(big_basket_url):
    return 1.5

def find_min_price(dict_of_site_url):

'''

        d = {'p_id': 'aa_1', 'p_name': 'Ashirvaad_aata', 'p_price': '270', 'source1': 'https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwa', 'op1': '265', 'source2': 'https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038', 'op2': '299', 'source3': 'https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-', 'op3': '235'}
        value= min(d.values())
        print(value)
        min_ = min(d, key=d.get)
        #min_ = min(d.items(), key= itemgetter(1))
'''

'''res = [key for key in d if
               all(d[temp] >= d[key]
                   for temp in d)]
        print("Keys with minimum values are : " + str(res))'''



#print_lists()

'''def aa_aata():


   reader = csv.reader("C:\\Users\\Sudheerk\\PycharmProjects\\sahi-keemat\\Grocery3_url_list.csv")
   with open("C:\\Users\\Sudheerk\\PycharmProjects\\sahi-keemat\\Grocery_url_list1.csv", newline='') as inFile:
    reader = csv.reader(inFile)'''

'''with open('coors_new.csv', mode='w') as outfile:
   writer = csv.writer(outfile)
     for rows in reader:
         k = rows[0]
         v = rows[2]
         mydict = {k:v for k in rows}
         print(mydict)'''

'''list1= []
 for row in reader:
    list1.append(row[2])
    print(row[2])

min_price= print(min(list1))
list1.append(row[3])
print(row[3])
list2 = list1.remove('offer_price')
print(list2)'''
'''min_price = min(list2)
print(min_price)
if list1(row[3]) == min_price:
   print(row[3])'''


'''def hello(url):
    print("https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad'")
    print("https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'")'''
'''def aashirwaad_aata( url,qty):
   print(f'{url},{qty}')'''

def product_details():
   page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
   soup = BeautifulSoup(page, 'html.parser')
   Bb_aashirwaad_aata = soup.find(class_="tQ1Iy")


