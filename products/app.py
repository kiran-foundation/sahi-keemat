import csv
import flask
import jinja2
import csv_files
from flask import Flask,render_template
from sahi_keemat_functions import product_details

app = Flask(__name__)

@app.route('/')

def post():
    """ Displays the index page accessible at '/'
    """

    headings = ("SiteName", "Url", "Price")
    products_data = product_details()
    return render_template('index.html',product_dict=products_data)

@app.route('/about')
def about():

        return render_template('home.html')


if __name__ == '__main__':
    app.debug =True
    app.run(host='0.0.0.0', port=4040)


