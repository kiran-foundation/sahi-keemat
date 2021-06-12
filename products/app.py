import csv
import flask
import jinja2
from flask import Flask,render_template
from sahi_keemat_functions import product_value,product_details

app = Flask(__name__)

headings = ("SiteName", "Url", "Price")
#data = product_value("csv_files/aata_new.csv")


#test_dict={list(product_list.keys())[0]: (a1,str(bb_price)),list(product_list.keys())[1]: (a2,str(jio_price))}

@app.route('/')
def post():
    """ Displays the index page accessible at '/'
    """
    products_data = product_details()
    return render_template('index.html',test_dict=products_data)


if __name__ == '__main__':

    app.debug =True
    app.run()
