import json

def database_lesen():
    data = {}
    try:
        with open('database.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

def eintrag_speichern(name, stunden, tage, lohn):
    database = database_lesen()
    database[name] = {"name": name, "hours": stunden, "days": tage, "salary": lohn}   
    print(database)
    with open('database.txt', "w", encoding="utf-8") as open_file:
        json.dump(database, open_file)

def eintrag_speichern_von_formular(form_request):
    print(form_request)
    name = form_request.get('name')
    hours = form_request.get('hours')
    days = form_request.get('days')
    salary = form_request.get('salary')
    eintrag_speichern(name, hours, days, salary)


def person_suchen(form_request):
    database = database_lesen()
    name = form_request.get('name')

    if name in database:
        return {name: database[name]}

    

