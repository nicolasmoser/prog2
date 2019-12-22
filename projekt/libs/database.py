import json

def database_read():
    data = {}
    try:
        with open('database.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

def database_save(data):
    open_file = open('database.txt', "w", encoding="utf-8")  
    data_formatted = json.dumps(data, indent=2)
    open_file.write(data_formatted)
    open_file.close()

def add_user(name, stunden, tage, lohn):
    data = database_read()
    data[name] = {"name": name, "hours": stunden, "days": tage, "salary": lohn}   
    print(data)
    database_save(data)

def get_user(name):
    database = database_read()
    if name in database:
        return database[name]
    else:
        return None

    

