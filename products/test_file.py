from new_test_file import bb_get_price,jio_get_price, flip_kart_get_price

URL = 'https://www.bigbasket.com/pd/126903/aashirvaad-atta-whole-wheat-5-kg-pouch/?nc=as&q=aashirwad'
f = open('C:\Users\Dell\Desktop\aata.csv','w')
f.write(URL)
#bb_get_price(URL)
#jio_get_price('https://www.jiomart.com/p/groceries/aashirvaad-whole-wheat-atta-5-kg/490000038')
#flip_kart_get_price('https://www.flipkart.com/aashirvaad-superior-mp-atta/p/itm2138546a91477?pid=FLREUC5PSFQUBHTC&lid=LSTFLREUC5PSFQUBHTCW8WKPS&marketplace=GROCERY&iid=97820c6c-0648-44fb-8b88-299fcdeed8eb.FLREUC5PSFQUBHTC.SEARCH')
f.write('\t')
f.write(bb_get_price(URL))
#f.write(jio_get_price(URL))
#f.write(flip_kart_get_price(URL))