import requests
import lxml
import textwrap
from bs4 import BeautifulSoup
import re
import csv
#import URLExtract
from csv import reader,DictReader,DictWriter,writer
from operator import itemgetter

from urlextract import urlextract_core

'''
<span class="_2j_7u">Rs <!-- -->244</span> atta 5 kg
<span class="_2j_7u">Rs <!-- -->239</span> sugar 5 kg
<span class="_2j_7u">Rs <!-- -->82</span> rice 1 kg
<span class="_2j_7u">Rs <!-- -->158.01</span> toor dal 1 kg


Jiomart Prices
<span class="final-price">Price: <span>₹ 210.00</span></span> atta 5 kg
<span class="final-price">Price: <span>₹ 213.00</span></span> sugar 5 kg
None rice 1 kg
<span class="final-price">Price: <span>₹ 136.00</span></span>  toor dal 1 kg
Flipkart Prices
<span class="u8dYXW">Special Price</span>
<span class="_22L9YP">₹<!-- -->211</span> sugar 5 kg



'''
def min_price(file_name):

    with open( file_name , 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)

        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        # print(list_of_dict)
        # test_product = list_of_dict[1]
        # print(test_product[6])

        products = dict()
        for item in list_of_dict:
            products[item['p_name']] = item
            # print(products[item['p_id']])
            data = products[item['p_name']]

            print(data)
            data_values = list(data.values())
            print(data_values)
            data_keys = list(data.keys())
            print(data_keys)


            data_keys = ['p_name' , 'op1' , 'op2' , 'op3']
            offer_priceList = [data[k] for k in data_keys if k in data]
            print(offer_priceList)

            data_keys = ['p_id' , 'source1' , 'source2' , 'source3']
            source_List = [data[k] for k in data_keys if k in data]
            print(source_List)

            new_List = dict(zip(source_List , offer_priceList))
            print(new_List)

            for item in list_of_dict:
                products = dict()

                products['p_id'] = item
                # print(products['AA1'])
                print(products)

            # min_values = min(offer_priceList)
            # print(min_values)
            print(min(new_List.items() , key=itemgetter(1)))
    return min(new_List.items() , key=itemgetter(1))



#with open("Aata_Url_Prices.csv","w") as f:
    #csv_writer = writer(f,lineterminator='\n')
 #   header=('p_name', 'source','price')
  #  csv_writer= DictWriter(f, fieldnames=header)
   # csv_writer.writerow(header)
f = open("Aata_Url_Prices.csv","w")
print('Aashirvaad-atta-Url-Prices')
page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
soup = BeautifulSoup(page,'html.parser')
Bb_aashirwaad_aata = soup.find(class_="_2j_7u")
print(Bb_aashirwaad_aata)
f = open("Aata_Url_Prices.csv","w")
#print('Aashirvaad-atta-Url-Prices')
page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
soup = BeautifulSoup(page,'html.parser')
Bb_aashirwaad_aata = soup.find(class_="_2j_7u")
print(Bb_aashirwaad_aata)
urldict = {}
products = [{'p_name': ' ', 'price':" " , 'source': " "}]
csvfile = open('Aata_Url_Prices.csv', 'w', newline='')
fields = list(products[0].keys())
obj = csv.DictWriter(csvfile,fieldnames=fields)
obj.writeheader()
obj.writerows(products)
#converted_price = float(re.sub(r"[^\d.]", "", Bb_aashirwaad_aata))
f.write('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad')
f.write('\t')
f.write('Bb_aashirwaad_aata')
f.write("\n")


page = requests.get('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038').text.encode('utf8').decode('ascii', 'ignore')
soup = BeautifulSoup(page,'html.parser')
jiomart_aashirwaad_aata = soup.find(class_="final-price")
print(jiomart_aashirwaad_aata)
f.write('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'  )
#f.write(str(jiomart_aashirwaad_aata))
f.write("\n")



page = requests.get('https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-299fcdeed8eb.FLREUC5PSFQUBHTC.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_ashirwaad_aata= soup.find(class_="_30jeq3 _16Jk6d")
#<div class="_3I9_wc _2p6lqe">₹<!-- -->270</div>
#fk_ashirwaad_aata.find('u8dYXW')
print(fk_ashirwaad_aata)
f.write('https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-299fcdeed8eb.FLREUC5PSFQUBHTC.SEARCH')
#f.write(str(fk_ashirwaad_aata))
f.write("\n")
#min_price("Aata_Url_Prices.csv")


f.close()


print('Madhur-Sugar-Url-Prices')

f1 = open("Sugar_Url_Prices.csv","w")

page = requests.get('https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur').text
soup = BeautifulSoup(page,'html.parser')
madhur_sugar = soup.find(class_='_2j_7u')
#madhur_sugar.find('_2ifWF')
print(madhur_sugar)
f1.write('sugar' )
f1.write('https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur' )
f1.write(str(madhur_sugar))

f1.write("\n")

page = requests.get('https://www.jiomart.com/p/groceries/madhur-pure-hygienic-sugar-5-kg/490861956').text
soup = BeautifulSoup(page,'html.parser')
jiomart_madhur_sugar = soup.find(class_="final-price")
#jiomart_madhur_sugar.find('price')
print(jiomart_madhur_sugar)
f1.write('https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur'  )
f1.write(str(jiomart_madhur_sugar))
f1.write("\n")

page = requests.get('https://www.flipkart.com/madhur-sugar/p/itmevjgp3vsgg77p?pid=SUGEUHHJAFPW8WKF&lid=LSTSUGEUHHJAFPW8WKFOHV5OR&marketplace=GROCERY&iid=0b60fb86-688b-43a0-9e7c-4ed44cc8c731.SUGEUD25B6YCCNGM.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_madhur_sugar = soup.find(class_="_30jeq3 _16Jk6d")#"_3I9_wc _2p6lqe")
print(fk_madhur_sugar)
f1.write('https://www.flipkart.com/madhur-sugar/p/itmevjgp3vsgg77p?pid=SUGEUHHJAFPW8WKF&lid=LSTSUGEUHHJAFPW8WKFOHV5OR&marketplace=GROCERY&iid=0b60fb86-688b-43a0-9e7c-4ed44cc8c731.SUGEUD25B6YCCNGM.SEARCH' )

#f.write(str(fk_madhur_sugar))
f1.write("\n")
f1.close()

f2 = open("Rice_Url_Prices.csv","w")
print('daawat-rozaana-Rice-Url-Prices')
page = requests.get('https://www.bigbasket.com/pd/255849/daawat-basmati-rice-rozana-gold-1-kg-pouch').text
soup = BeautifulSoup(page,'html.parser')
daawat_rozaana = soup.find(class_ ='_2j_7u')
#daawat_rozaana.find('_2ifWF')
print(daawat_rozaana)

f2.write('https://www.bigbasket.com/pd/255849/daawat-basmati-rice-rozana-gold-1-kg-pouch' )
f2.write(str(daawat_rozaana))
f2.write("\n")


page = requests.get('https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714').text
soup = BeautifulSoup(page,'html.parser')
jiomart_daawat_rozana= soup.find(class_="final-price")
print(jiomart_daawat_rozana)

f2.write('https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714'  )
#f.write(str(jiomart_daawat_rozana))
f2.write("\n")

page = requests.get('https://www.flipkart.com/daawat-rozana-gold-basmati-rice-medium-grain/p/itm87d2a5d167c48?pid=RICEUC2YGGQJTXHD&lid=LSTRICEUC2YGGQJTXHDITCFX4&marketplace=GROCERY&q=daawat+rozana+gold+basmati+rice&store=eat%2Fyul&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&fm=SEARCH&iid=6761dc6b-e628-4b5f-8064-2bbd9ca6589e.RICEUC2YGGQJTXHD.SEARCH&ppt=sp&ppn=sp&ssid=tthg94h5680000001615895215977&qH=91caef11422b600e').text
soup = BeautifulSoup(page,'html.parser')
fk_dawat_rozana = soup.find(class_="_30jeq3 _16Jk6d")
print(fk_dawat_rozana)


f2.write('https://www.flipkart.com/daawat-rozana-gold-basmati-rice-medium-grain/p/itm87d2a5d167c48?pid=RICEUC2YGGQJTXHD&lid=LSTRICEUC2YGGQJTXHDITCFX4&marketplace=GROCERY&q=daawat+rozana+gold+basmati+rice&store=eat%2Fyul&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&fm=SEARCH&iid=6761dc6b-e628-4b5f-8064-2bbd9ca6589e.RICEUC2YGGQJTXHD.SEARCH&ppt=sp&ppn=sp&ssid=tthg94h5680000001615895215977&qH=91caef11422b600e' )
#f.write(str(fk_dawat_rozana))
f2.write("\n")
f2.close()

print('tata-sampann-toordal-Url-Prices')
f2 = open("Dal_Url_Prices.csv","w")
page = requests.get('https://www.bigbasket.com/pd/40000291/tata-sampann-toor-dal-1-kg').text
soup = BeautifulSoup(page,'html.parser')
tata_sampann_toordal = soup.find(class_='_2j_7u')
print(tata_sampann_toordal)

f2.write('https://www.bigbasket.com/pd/40000291/tata-sampann-toor-dal-1-kg' )
f2.write(str(tata_sampann_toordal))
f2.write("\n")

page = requests.get('https://www.jiomart.com/p/groceries/tata-sampann-high-protein-unpolished-tur-arhar-dal-1-kg/490830932').text
soup = BeautifulSoup(page,'html.parser')
jiomart_tatasampann_toordaal= soup.find(class_="final-price")
print(jiomart_tatasampann_toordaal)


f2.write('https://www.jiomart.com/p/groceries/tata-sampann-high-protein-unpolished-tur-arhar-dal-1-kg/490830932' )
#f.write(str(jiomart_tatasampann_toordaal))
f2.write("\n")

page = requests.get('https://www.flipkart.com/tata-sampann-toor-dal-1-kg-moong/p/itm8006fc6fe0be1?pid=PLSFQAYUWYVDZECN&lid=LSTPLSFQAYUWYVDZECN0FOQZK&marketplace=GROCERY&iid=08c05eea-e9dc-402c-be71-c2e2b5ad36b4.PLSFQAYUWYVDZECN.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_toor_dal = soup.find(class_="_30jeq3 _16Jk6d")
print(fk_toor_dal)
fk_url1 ='https://www.flipkart.com/tata-sampann-toor-dal-1-kg-moong/p/itm8006fc6fe0be1?pid=PLSFQAYUWYVDZECN&lid=LSTPLSFQAYUWYVDZECN0FOQZK&marketplace=GROCERY&iid=08c05eea-e9dc-402c-be71-c2e2b5ad36b4.PLSFQAYUWYVDZECN.SEARCH'
#newfk_url = textwrap.shorten(fk_url1, width=20)
#f.write(fk_url1)
#f.write('https://www.flipkart.com/tata-sampann-toor-dal-1-kg-moong/p/itm8006fc6fe0be1?pid=PLSFQAYUWYVDZECN&lid=LSTPLSFQAYUWYVDZECN0FOQZK&marketplace=GROCERY&iid=08c05eea-e9dc-402c-be71-c2e2b5ad36b4.PLSFQAYUWYVDZECN.SEARCH' )
#f.write(str(fk_toor_dal))
f2.write("\n")
f2.close()

import csv
d = {}
with open('Grocery_url_list.csv') as f:
    for key, *values in csv.reader(f):
        d[key] = tuple(map(str, values))
    print(d)