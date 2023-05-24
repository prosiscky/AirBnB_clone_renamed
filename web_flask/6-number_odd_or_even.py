#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homePage():
    """ Defines home page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Defines hbnb page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cdisplayPage(text):
    """ Define c page """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
def pythonDefault():
    """ Define Python page """
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def pythondisplayPage(text):
    """ Define python page """
    if not text:
        return redirect(url_for('/python'))
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def numDisplay(n):
    """ Define a dyamic page """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplateView(n):
    """ Define a dyamic page """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddEvenTemplateView(n):
    """ Define a dyamic page """
    if n % 2 == 0:
        text = "{} is even".format(n)
    else:
        text = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', odd_or_even=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
