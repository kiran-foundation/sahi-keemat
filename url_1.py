import requests
import lxml
from bs4 import BeautifulSoup


print('Big-Basket-Prices')
page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
soup = BeautifulSoup(page,'html.parser')
Bb_aashirwaad_aata = soup.find(class_="tQ1Iy")
print(dir(Bb_aashirwaad_aata))
print(Bb_aashirwaad_aata.text)
#aashirwaad_aata1.find('')
''''
page = requests.get('https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur').text
soup = BeautifulSoup(page,'html.parser')
madhur_sugar = soup.find(class_='_2ifWF')
#madhur_sugar.find('_2ifWF')
print(madhur_sugar)

page = requests.get('https://www.bigbasket.com/pd/255849/daawat-basmati-rice-rozana-gold-1-kg-pouch').text
soup = BeautifulSoup(page,'html.parser')
daawat_rozaana = soup.find(class_ ='_2ifWF')
#daawat_rozaana.find('_2ifWF')
print(daawat_rozaana)

page = requests.get('https://www.bigbasket.com/pd/40000291/tata-sampann-toor-dal-1-kg').text
soup = BeautifulSoup(page,'html.parser')
tata_sampann_toordal = soup.find(class_='_2ifWF')
print(tata_sampann_toordal)


#Jiomart data
print("Jiomart Prices")
page = requests.get('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038').text
soup = BeautifulSoup(page,'html.parser')
jiomart_aashirwaad_aata1= soup.find(class_= "price")
print(jiomart_aashirwaad_aata1)

page = requests.get('https://www.jiomart.com/p/groceries/madhur-pure-hygienic-sugar-5-kg/490861956').text
soup = BeautifulSoup(page,'html.parser')
jiomart_madhur_sugar = soup.find(class_="price")
#jiomart_madhur_sugar.find('price')
print(jiomart_madhur_sugar)

page = requests.get('https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714').text
soup = BeautifulSoup(page,'html.parser')
jiomart_daawat_rozana= soup.find(class_="price")
print(jiomart_daawat_rozana)

page = requests.get('https://www.jiomart.com/p/groceries/tata-sampann-high-protein-unpolished-tur-arhar-dal-1-kg/490830932').text
soup = BeautifulSoup(page,'html.parser')
jiomart_tatasampann_toordaal= soup.find(class_="price")
print(jiomart_tatasampann_toordaal)

#tata_sampann_toordal.find('_2ifWF')


#for aashirwaad_aata in aashirwaad_aata_list_item:
    #print(aashirwaad_aata.prettify())

#Flip-kart-Prices
print("Flipkart Prices")
page = requests.get('https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-299fcdeed8eb.FLREUC5PSFQUBHTC.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_ashirwaad_aata= soup.find(class_="_3I9_wc _2p6lqe")
#<div class="_3I9_wc _2p6lqe">₹<!-- -->270</div>
fk_ashirwaad_aata.find('_3I9_wc _2p6lqe')
print(fk_ashirwaad_aata)

page = requests.get('https://www.flipkart.com/madhur-sugar/p/itmevjgp3vsgg77p?pid=SUGEUHHJAFPW8WKF&lid=LSTSUGEUHHJAFPW8WKFOHV5OR&marketplace=GROCERY&iid=0b60fb86-688b-43a0-9e7c-4ed44cc8c731.SUGEUD25B6YCCNGM.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_madhur_sugar = soup.find(class_="_3I9_wc _2p6lqe")
print(fk_madhur_sugar)

page = requests.get(https://www.flipkart.com/daawat-rozana-gold-basmati-rice-medium-grain/p/itm87d2a5d167c48?pid=RICEUC2YGGQJTXHD&lid=LSTRICEUC2YGGQJTXHDITCFX4&marketplace=GROCERY&q=daawat+rozana+gold+basmati+rice&store=eat%2Fyul&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_12_sc_na_na&fm=SEARCH&iid=6761dc6b-e628-4b5f-8064-2bbd9ca6589e.RICEUC2YGGQJTXHD.SEARCH&ppt=sp&ppn=sp&ssid=tthg94h5680000001615895215977&qH=91caef11422b600e.text
soup = BeautifulSoup(page,'html.parser')
fk_dawat_rozana = soup.find(class_="_3I9_wc _2p6lqe")
print(fk_dawat_rozana)

page = requests.get('https://www.flipkart.com/tata-sampann-toor-dal-1-kg-moong/p/itm8006fc6fe0be1?pid=PLSFQAYUWYVDZECN&lid=LSTPLSFQAYUWYVDZECN0FOQZK&marketplace=GROCERY&iid=08c05eea-e9dc-402c-be71-c2e2b5ad36b4.PLSFQAYUWYVDZECN.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_toor_dal = soup.find(class_="_3I9_wc _2p6lqe")
print(fk_toor_dal)



#<span id="final_price">₹ 60.00</span>
'''