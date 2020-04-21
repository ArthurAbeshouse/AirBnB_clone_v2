#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """ Closes the database """
    storage.close()


@app.route("/cities_by_states")
def states_list():
    """ Lists all the states """
    states = list(storage.all(State).values())
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
