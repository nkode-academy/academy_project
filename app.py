from flask import Flask

app = Flask(__name__)
counter = 0


@app.route("/")
def hello_world():
    global counter
    counter = counter + 1
    return "<p>juhu dies ist der first versuch{}</p>".format(counter)


@app.route("/bye/123")
def good_bye():
    return "goodbye"
