#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    """ Routes an index """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Routes /hbnb """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """ Routes /c/<text> """
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python_text(text):
    """ Routes /python/<text> """
    return "Python " + text.replace("_", " ")

if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
