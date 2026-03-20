import addcon
import viewcon 
import upcon
import delcon 
import storage
storage.load_contacts()

print("Hello User....")
print("Welcome To Contact Book......")
print()

while True:
  print("1. Create A New Contact.")
  print("2. View All Contacts.")
  print("3. Update A Contact.")
  print("4. Delete A Contact.")
  print("5. Exit.")
  print("")
  choice = input("Enter A Choice:  ")
  
  if choice == '1' :
    addcon.add_con()
  elif choice == '2' :
    viewcon.view_con()
  elif choice == '3' :
    upcon.up_con()
  elif choice == '4' :
    delcon.del_con()
  elif choice == '5' :
    break
  else:
    print("Invalid Input.....")