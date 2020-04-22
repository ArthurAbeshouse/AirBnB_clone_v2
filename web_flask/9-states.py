#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception):
    """ Closes the database """
    storage.close()


@app.route("/states")
@app.route("/states/<state_id>")
def states_list(state_id=None):
    """ Lists all the states """
    if state_id is not None:
        states = storage.all(State)
        state_id = "States.{}".format(state_id)
    else:
        states = list(storage.all(State).values())
    return render_template("9-states.html", states=states, state_id=state_id)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
