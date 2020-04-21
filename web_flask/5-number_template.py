#!/usr/bin/python3

from flask import Flask, render_template
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


@app.route("/number/<int:n>")
def number(n):
    """ Routes /number/<n> """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ Routes /number_template/<n> """
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
