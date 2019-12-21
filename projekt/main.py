from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import database

app = Flask("database")

@app.route("/")
@app.route("/index")
def index():
    telbuchdaten = database.database_lesen()
    return render_template("database.html", telbuch=telbuchdaten)


@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    if (request.method == 'POST'):
        person_eintrag = database.person_suchen(request.form)
        name = request.form.get('name')
        print(person_eintrag)
        return render_template("tracker.html", value=person_eintrag[name])

    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST']) 
def add():
    if (request.method == 'POST'):
        database.eintrag_speichern_von_formular(request.form)
        return redirect("/")

    return render_template("add.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)