# myflaskapp/__init__.py

from flask import Flask

#Create a Flask web application
app = Flask(__name__)

# Define a route with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
