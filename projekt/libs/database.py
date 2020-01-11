import json
import time

def database_read(): # Funktion, die die Datenbank liest
    data = {} # Leeres Dicitionary erstellen mit der Bennenung "data".
    try:
        with open('database.txt', "r") as open_file: # Öffnet und liest die Textdatei "database.txt". "r" bedeutet, dass wir die Datei nur lesen.
            data = json.load(open_file) # konvertiert Dateiinhalt in das Dicitonary
    except:
        print("Error with file!") 
    finally:
        return data # Gibt Dicitionary "data" mit allen Usern und deren Datan zurück.

def database_save(data): # Funktion, die ein erhaltenes Dicitonary mit neuen Userdaten in das Textfile "database.txt" speichert
    open_file = open('database.txt', "w", encoding="utf-8") # Öffnet die Textdatei "database.txt". "w" bedeutet, dass wir in die Datei schreiben.
    data_formatted = json.dumps(data, indent=2) # Erhaltene Daten werden bearbeitet, um sie besser lesbar und einheitlich zu machen
    open_file.write(data_formatted) # Neue Datei wird der Textdatei "database.txt" hinugefügt.
    open_file.close()

def add_user(name, stunden, tage, lohn): # Funktion, die Daten vom User erhält und diese in die Datenbank speichert.
    data = database_read() # Alle Daten von Datenbank werden gelesen
    data[name] = {"name": name, "hours": stunden, "days": tage, "salary": lohn} # Neuer User wird der Datenbank hinzugefügt.
    print(data)
    database_save(data) # Speichert neue Daten in die Textdatei.

def get_user(name): # Funktion, die den Usernamen von der Datenbank ausgibt
    database = database_read() # Alle Daten von Datenbank werden gelesen
    if name in database: # Prüfen, ob der Name in der Datenbank existiert
        return database[name] # Wenn ja, gibt er die Daten der Person zurück.
    else:
        return None # Wenn nein, gibt er nichts zurück.

    
def start_time(name): # Funktion, die einem bestehenden User ein neuen Datensatz hinzufügt (Uhrzeit)
    users_data = database_read() # Alle Daten von Datenbank werden gelesen
    if name in users_data: # Prüfen, ob der Name in der Datenbank existiert
        users_data[name]["start_time"] = int(time.time()) # Wenn ja, fügt neuen Datensatz "start_time" zum User hinzu: Value ist die momentane Uhrzeit
        database_save(users_data) # Speichert neue Daten in die Textdatei.

def end_time(name):
    users_data = database_read() # Alle Daten von Datenbank werden gelesen
    if name in users_data: # Prüfen, ob der Name in der Datenbank existiert
        user = users_data[name]
        users_data[name]['end_time'] = int(time.time()) # Wenn ja, fügt neuen Datensatz "end_time" zum User hinzu: Value ist die momentane Uhrzeit
        if 'total_time' not in user: # Wenn der Datensatz "total_time" nicht im User existiert, dann den Datensatz mit dem Wert 0 hinzufügen
            user['total_time'] = 0
        else:
            user['total_time'] = user['total_time'] + (user['end_time'] - user['start_time']) # Sonst, aus den beiden Uhrzeiten berechnen und mit dem bestehenden Wert addieren
        database_save(users_data) # Speichert neue Daten in die Textdatei.

def reset_day(name):
    users_data = database_read()
    if name in users_data:
        if 'start_time' in users_data[name]:
            del users_data[name]['start_time']
        if 'end_time' in users_data[name]:
            del users_data[name]['end_time']
        database_save(users_data)

def reset_month(name):
    users_data = database_read()
    if name in users_data:
        if 'start_time' in users_data[name]:
            del users_data[name]['start_time']
        if 'end_time' in users_data[name]:
            del users_data[name]['end_time']
        if 'total_time' in users_data[name]:
            del users_data[name]['end_time']
        database_save(users_data)