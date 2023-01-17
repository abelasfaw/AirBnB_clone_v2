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


@app.route('/c/<text>', strict_slashes=False)
def c_handler(text):
    """returns C followed by the value of the text variable and
    replaces underscore _ symbols with a space from <text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_handler(text="is cool"):
    """returns Python followed by the value of the text variable and
    replaces underscore _ symbols with a space from <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_handler(n):
    """returns n is a number if n is an integer"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
