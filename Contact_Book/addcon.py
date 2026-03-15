from cons import contacts
from storage import save_contacts

def add_con():
   name = input("Enter Name: ")
   if name in contacts :
      print("Name Already Exists.......")
   else:
      num = input("Enter Number:")
      age = input("Enter Age:")
      contacts[name] = {'age':age , 'num':num}
      print(f"Contact {name} Has Been Saved...")
      save_contacts()