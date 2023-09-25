#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage
from models.amenity import Amenity

app = Flask(__name__)
amenities = storage.all(Amenity).values()
for amenity in amenities:
    print(amenity.name)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """ This function closes the session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_objects():
    """ This function renders the template 10-hbnb_filters.html"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
