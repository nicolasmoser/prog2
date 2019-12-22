from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import database

app = Flask("database")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/database_data")
def database_data():
    users_data = database.database_read()
    return render_template("database.html", users=users_data)
    

@app.route("/add", methods=['GET', 'POST']) 
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        name = request.form.get('name')
        hours = request.form.get('hours')
        days = request.form.get('days')
        salary = request.form.get('salary')
        database.add_user(name, hours, days, salary)
        return redirect(url_for('index'))

    



if __name__ == "__main__":
    app.run(debug=True, port=5000)