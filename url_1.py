import requests
import lxml
from bs4 import BeautifulSoup
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
#aashirwaad_aata_list_item = aashirwaad_aata.find_all('price')

#for aashirwaad_aata in aashirwaad_aata_list_item:
    #print(aashirwaad_aata.prettify())




