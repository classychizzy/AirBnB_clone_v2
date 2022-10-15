#!/usr/bin/python3
"""an app that uses flask to display text on the browser
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


"""configures the port and ip of the flask app"""
app.run(host="0.0.0.0", port=5000)
