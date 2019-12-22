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

@app.route("/login", methods=['POST'])
def login():
    name = request.form.get('name')
    user_data = database.get_user(name)
    if user_data:
        return redirect(url_for('tracker', name=name))
    else:
        return redirect(url_for('index'))

@app.route('/tracker')
def tracker():
    name = request.args.get('name')
    user_data = database.get_user(name)
    if 'start_time' in user_data and 'end_time' in user_data:
        return redirect (url_for('result', name=name))
    else:
        return render_template("tracker.html", user=user_data)
 


if __name__ == "__main__":
    app.run(debug=True, port=5000)