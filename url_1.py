import requests
import lxml
from bs4 import BeautifulSoup
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
#aashirwaad_aata_list_item = aashirwaad_aata.find_all('price')

#for aashirwaad_aata in aashirwaad_aata_list_item:
    #print(aashirwaad_aata.prettify())




