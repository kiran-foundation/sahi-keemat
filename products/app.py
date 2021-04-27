import flask
from flask import Flask,render_template


# Create the application.
app = Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()

from jinja2 import Template

name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)
