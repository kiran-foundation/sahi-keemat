import requests
import lxml
from bs4 import BeautifulSoup

print('Big-Basket-Prices')
page = requests.get('https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad').text
soup = BeautifulSoup(page,'html.parser')
aashirwaad_aata = soup.find(class_="tQ1Iy")
#aashirwaad_aata.find('tQ1Iy')
print(aashirwaad_aata)
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
#tata_sampann_toordal.find('_2ifWF')
print(tata_sampann_toordal)

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

print("flipkart-prices")



#<span id="final_price">₹ 60.00</span>