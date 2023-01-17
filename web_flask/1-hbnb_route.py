#!/usr/bin/python3
"""starts a flas web application on port 5000"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_handler():
    """returns Hello HBNB! when request hits / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_handler():
    """returns HBNB when request hits /hbnb route"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
