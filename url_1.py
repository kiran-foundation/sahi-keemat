import requests
import lxml
from bs4 import BeautifulSoup


print('Big-Basket-Prices')
page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
soup = BeautifulSoup(page,'html.parser')
Bb_aashirwaad_aata = soup.find(class_="tQ1Iy")
print(Bb_aashirwaad_aata)
#aashirwaad_aata1.find('')

page = requests.get('https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur').text
soup = BeautifulSoup(page,'html.parser')
madhur_sugar = soup.find(class_='_2ifWF')
#madhur_sugar.find('_2ifWF')
print(madhur_sugar)

page = requests.get('https://www.bigbasket.com/pd/204005/daawat-basmati-rice-rozana-gold-5-kg-pouch').text
soup = BeautifulSoup(page,'html.parser')
daawat_rozaana = soup.find(class_ ='_2ifWF')
#daawat_rozaana.find('_2ifWF')
print(daawat_rozaana)

page = requests.get('https://www.bigbasket.com/pd/40000291/tata-sampann-toor-dal-1-kg').text
soup = BeautifulSoup(page,'html.parser')
tata_sampann_toordal = soup.find(class_='_2ifWF')

#Jiomart data
page = requests.get('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038').text
soup = BeautifulSoup(page,'html.parser')
jiomart_aashirwaad_aata1= soup.find(class_= "price")
print(jiomart_aashirwaad_aata1)

page = requests.get('https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714').text
soup = BeautifulSoup(page,'html.parser')
jiomart_daawat_rozana= soup.find(class_="price")
print(jiomart_daawat_rozana)

page = requests.get('https://www.jiomart.com/p/groceries/tata-sampann-high-protein-unpolished-tur-arhar-dal-1-kg/490830932').text
soup = BeautifulSoup(page,'html.parser')
jiomart_tatasampann_toordaal= soup.find(class_="price")
print(jiomart_tatasampann_toordaal)

page = requests.get('https://www.jiomart.com/p/groceries/madhur-pure-hygienic-sugar-5-kg/490861956').text
soup = BeautifulSoup(page,'html.parser')
jiomart_madhur_sugar = soup.find(class_="price")
#jiomart_madhur_sugar.find('price')
print(jiomart_madhur_sugar)

#tata_sampann_toordal.find('_2ifWF')
print(tata_sampann_toordal)

#for aashirwaad_aata in aashirwaad_aata_list_item:
    #print(aashirwaad_aata.prettify())

#grofers
page = requests.get('https://grofers.com/prn/daawat-rozana-super-basmati-rice/prid/10974').text
soup = BeautifulSoup(page,'html.parser')
daawat_rozana = soup.find(class_="pdp-product__price--old")
print(daawat_rozana)

#jiomart
print("Jiomart-Prices")
page = requests.get('https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714').text
soup = BeautifulSoup(page,'html.parser')
jiomart_daawat_rozana = soup.find(class_="price")
print(jiomart_daawat_rozana)

page = requests.get('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038').text
soup = BeautifulSoup(page,'html.parser')
jiomart_aashirwaad_aata = soup.find(class_="price")
jiomart_aashirwaad_aata.find('price')
print(jiomart_aashirwaad_aata)

page = requests.get('https://www.jiomart.com/p/groceries/madhur-pure-hygienic-sugar-5-kg/490861956').text
soup = BeautifulSoup(page,'html.parser')
jiomart_madhur_sugar = soup.find(class_="price")
jiomart_madhur_sugar.find('price')
print(jiomart_madhur_sugar)

page = requests.get('https://www.jiomart.com/p/groceries/tata-sampann-high-protein-unpolished-tur-arhar-dal-1-kg/490830932').text
soup = BeautifulSoup(page,'html.parser')
tur_dal= soup.find(class_="price")
tur_dal.find('price')
print(tur_dal)


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

page = requests.get('https://www.flipkart.com/daawat-rozana-super-basmati-rice-medium-grain/p/itmf786kvkpc2gzy?pid=RICEUC2Y2FPTSNU9&lid=LSTRICEUC2Y2FPTSNU9JPDYCC&marketplace=GROCERY&iid=38e00334-d786-4a86-9664-8a9f42fe3274.RICEUC2Y2FPTSNU9.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_dawat_rozana = soup.find(class_="_3I9_wc _2p6lqe")
print(fk_dawat_rozana)

page = requests.get('https://www.flipkart.com/flipkart-supermart-select-toor-dal-split/p/itmf2ujjpnsasqzv?pid=PLSEXBGTFTVU23FQ&lid=LSTPLSEXBGTFTVU23FQTWWU5S&marketplace=GROCERY&iid=987edc55-da48-4886-af5a-5dbfda6f5aa8.PLSEWWBTMKE2N362.SEARCH').text
soup = BeautifulSoup(page,'html.parser')
fk_toor_dal = soup.find(class_="_30jeq3 _16Jk6d")
print(fk_toor_dal)



#<span id="final_price">₹ 60.00</span>
