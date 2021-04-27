import csv
from csv import reader,DictReader,DictWriter,writer
from operator import itemgetter

from sahi_keemat_functions import bb_get_price,jio_get_price,get_converted_price,new_csv,append_data,product_value


product_value("url_list.csv")

new_csv("atta.csv")

#url= 'https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'
url_a = 'https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad'
append_data("atta.csv",url_a,str(bb_get_price(url_a)))
url_a1= 'https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038'
append_data("atta.csv",url_a1,str(jio_get_price(url_a1)))

test_dict = {url_a:str(bb_get_price(url_a)),url_a1:str(jio_get_price(url_a1))}
print(test_dict)
min_price = {(min(test_dict.items(), key=itemgetter(1)))}
print("Sahi-Keemat for the product available here: ", min_price)

new_csv("sugar.csv")

url_s = 'https://www.bigbasket.com/pd/214431/madhur-sugar-refined-5-kg-pouch/?nc=as&q=madhur'
append_data("sugar.csv",url_s,str(bb_get_price(url_s)))
url_s1 = 'https://www.jiomart.com/p/groceries/madhur-pure-hygienic-sugar-5-kg/490861956'
append_data("sugar.csv",url_s1,str(jio_get_price(url_s1)))

test_dict = {url_s:str(bb_get_price(url_s)),url_s1:str(jio_get_price(url_s1))}
print(test_dict)
min_price = {(min(test_dict.items(), key=itemgetter(1)))}
print("Sahi-Keemat for the product available here: ", min_price)

new_csv("rice.csv")

url_r = 'https://www.bigbasket.com/pd/255849/daawat-basmati-rice-rozana-gold-1-kg-pouch'
append_data("rice.csv",url_r,str(bb_get_price(url_r)))
url_r1 = 'https://www.jiomart.com/p/groceries/daawat-rozana-super-basmati-rice-1-kg/490863714'
append_data("rice.csv",url_r1,str(jio_get_price(url_r1)))

test_dict = {url_r:str(bb_get_price(url_r)),url_r1:str(jio_get_price(url_r1))}
print(test_dict)
min_price = {(min(test_dict.items(), key=itemgetter(1)))}
print("Sahi-Keemat for the product available here: ", min_price)

