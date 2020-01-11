from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import database

app = Flask("database")

@app.route("/")
def index():
    return render_template("index.html") # Hier übertragen wir die "index.html" Seite

@app.route("/database_data")
def database_data():
    users_data = database.database_read() # Liest alles Datenbank Daten und überträgt sie zu "database.html" 
    return render_template("database.html", users=users_data)


@app.route("/add", methods=['GET', 'POST']) 
def add():
    if request.method == 'GET': 
        return render_template("add.html") # Wenn Methode = GET, dann übertragen wir die "add.html" Seite.
    else:
        name = request.form.get('name')
        hours = request.form.get('hours')
        days = request.form.get('days')
        salary = request.form.get('salary')
        database.add_user(name, hours, days, salary) # Hier holen wir die Daten von der Form und fügen Sie dem Nutzer hinzu.
        return redirect(url_for('index')) # Index Seite wird zurückgegeben/geöffnet.

@app.route("/login", methods=['POST'])
def login():
    name = request.form.get('name') # Username wird von der form geholt
    user_data = database.get_user(name) # Dieser Name wird genutzt um die dazugehörigen Daten von der Datnebank zu holen
    if user_data:
        return redirect(url_for('tracker', name=name)) # Wenn der User existiert, verlinken wir zur Tracker Seite
    else:
        return redirect(url_for('index')) # Wenn ncht, dann zurück zum Index / Startseite

@app.route('/tracker')
def tracker():
    name = request.args.get('name') # Hier holen wir den Namen von der URL
    user_data = database.get_user(name) # Dieser Name wird genutzt um die dazugehörigen Daten von der Datnebank zu holen
    if 'start_time' in user_data and 'end_time' in user_data:
        return redirect (url_for('result', name=name)) # Sollte man bereits in der Resultatseite sein und das Prgram schliesst, wird man beim Öffnen und nach dem Login direkt zur Resultatseite kommen.
    else:
        return render_template("tracker.html", user=user_data) # Wenn Start- und Endzeit noch nicht existieren, kommt man zur Trackerseite.

@app.route("/start", methods=['POST'])
def start():
    name = request.args.get('name') # Username von URL holen
    database.start_time(name) # Datzensatz "start_time" den Userdaten hinzufügen
    return redirect(url_for('tracker', name=name)) # Redirect zur Trackerseite

@app.route("/end", methods=['POST'])
def end():
    name = request.args.get('name') # Username von URL holen
    database.end_time(name) # Datzensatz "end_time" den Userdaten hinzufügen
    return redirect(url_for('result', name=name)) # Redirect zur Resultatseite

@app.route("/result")
def result():
    name = request.args.get('name') # Username von URL holen
    user = database.get_user(name) # Daten des User holen
    hours = int(user['hours']) # Aus Daten integer machen 
    days = int(user['days']) # Aus Daten integer machen 
    rate = int(user['salary']) # Aus Daten integer machen 
    goal = hours * days * 60 * 60 # Aus Daten monatliches Arbeitsziel in Stunden berechnen
    current_time = user['end_time'] - user['start_time'] # Arbeitszeit des Tages berechnen
    total_time = user['total_time'] # Gesamte Arbeitszeit des Monats
    workload = round(total_time / goal, 2) * 100 # Resultat in Prozent auf 2 Kommastellen nach Punkt berechnen
    current_hours = current_time // (60 * 60)  # Arbeitszeit des Tages in Stunden
    current_minutes = current_time // 60 - current_hours * 60 # Arbeitszeit des Tages: übrige Minuten
    overtime = current_time - hours * 60 * 60 # Überstunden des Tages berechnen
    if overtime > 0: # Überzeit nur berechnen, wenn grösser als 0.
        overtime_hours = overtime // (60 * 60)
        overtime_minutes = overtime // 60 - overtime_hours * 60
    else:
        overtime_hours = 0
        overtime_minutes = 0
    overtime_month = total_time - goal
    if overtime_month > 0: # Überzeit nur berechnen, wenn grösser als 0.
        overtime_month_hours = overtime_month // (60 * 60)
        overtime_month_minutes = overtime_month // 60 - overtime_month_hours * 60
    else:
        overtime_month_hours = 0
        overtime_month_minutes = 0
    earnings = total_time // (60 * 60) * rate # Bereits verdientes Geld des Monats berechnen
    goal_earnings = hours * days * rate # Angestrebtes Gehalt berechnen
    return render_template(
        'result.html',
        user=user,
        workload=workload,
        current_hours=current_hours,
        current_minutes=current_minutes,
        overtime_hours=overtime_hours,
        overtime_minutes=overtime_minutes,
        overtime_month_hours=overtime_month_hours,
        overtime_month_minutes=overtime_month_minutes,
        earnings=earnings,
        goal=goal,
        overtime=overtime,
        goal_earnings=goal_earnings
    ) # Gibt Daten / Zahlen an Resultatseite weiter

@app.route("/new-day")
def new_day():
    name = request.args.get('name') # Username von URL holen
    database.FUNKTION
    return redirect(url_for('tracker', name=name))

@app.route("/new-month")
def new_day():
    name = request.args.get('name') # Username von URL holen
    database.FUNKTION
    return redirect(url_for('tracker', name=name))

if __name__ == "__main__":
    app.run(debug=True, port=5000)