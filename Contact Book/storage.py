import json
from cons import contacts

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            data = json.load(f)
            contacts.update(data)
    except FileNotFoundError:
        pass