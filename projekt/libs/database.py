import json

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

    

