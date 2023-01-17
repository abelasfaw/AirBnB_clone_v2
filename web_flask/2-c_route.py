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


@app.route('/c/<text>')
def c_handler(text):
    """returns C followed by the value of the text variable and
	replaces underscore _ symbols with a space from <text>"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
