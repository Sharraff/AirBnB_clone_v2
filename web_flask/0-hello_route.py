<<<<<<< HEAD
#!/usr/bin/python3
"""
Flask framework
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
=======
# myFlaskapp/0-hello_route.py
from  . import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> a39737ea071311457f4c1460ae8178f3926fd7c0
