from cons import contacts 
from storage import save_contacts

def del_con():
   name = input("Enter Name: ")
   if name in contacts:
     del contacts[name]
     print(f"{name} Has Been Deleted.....")
     save_contacts()
   else:
     print("Sorry...Could Not Find Such Contact....")