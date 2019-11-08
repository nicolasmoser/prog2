from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import telefonbuch

app = Flask("Telefonbuch")

@app.route("/")
@app.route("/index")
def index():
    return render_template("telefonbuch.html")

@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    return "search"

@app.route("/add", methods=['GET', 'POST']) 
def add():
    return "add"

if __name__ == "__main__":
    app.run(debug=True, port=5000)