#!/usr/bin/python3

from flask import Flask, render_template
from models import storage, Amenity
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """ Closes the database """
    storage.close()


@app.route("/hbnb_filters")
def hbnb_filters():
    """ Makes web page interactive """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
