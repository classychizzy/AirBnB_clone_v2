#!/usr/bin/python3
"""an app that uses flask to display text on the browser
"""


from flask import Flask
app = Flask(__name__)
"""Flask application instance
"""


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """hello page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """c page"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
def Python_text(text):
    """c page"""
    return 'Python {}'.format(text.replace('_', ' '))


"""configures the port and ip of the flask app"""
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
