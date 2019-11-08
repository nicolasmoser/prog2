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
    telbuchdaten = telefonbuch.telefonbuch_lesen()
    return render_template("telefonbuch.html", telbuch=telbuchdaten)


@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    if (request.method == 'POST'):
        person_eintrag = telefonbuch.person_suchen(request.form)
        print(person_eintrag)
        return render_template("telefonbuch.html", telbuch=person_eintrag)

    return render_template("search.html")

@app.route("/add", methods=['GET', 'POST']) 
def add():
    if (request.method == 'POST'):
        telefonbuch.eintrag_speichern_von_formular(request.form)
        return redirect("/")

    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)