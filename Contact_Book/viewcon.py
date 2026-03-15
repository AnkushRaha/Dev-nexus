from cons import contacts
from storage import save_contacts

def view_con():
   y = len(contacts)
   print("All Contacts : ",y)
   name = input("Search: ")
   if name in contacts:
     x = contacts[name]
     print(x)
     save_contacts()
   else: 
     print("Sorry...Can Not Find The Contact....")