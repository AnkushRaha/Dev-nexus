from cons import contacts
from storage import save_contacts

def up_con():
   name = input("Enter Name: ")
   if name in contacts :
      num = input("Enter Updated Number:")
      age = input("Enter Updated Age:")
      contacts[name] = {'age' : int(age), 'num' : num}
      print(f"Contact {name} Has Been Updated...")
      save_contacts()
   else:
      print("Sorry.....Could Not Find Any Contact....")