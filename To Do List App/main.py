import func 

print("WELCOME USER! ")
while True:
  print("1. Add Task.")
  print("2. View Task.")
  print("3. Delete Task.")
  print("4. Exit.")
  choice = int(input("Enter Your Choice (1, 2, 3, 4):    "))
  if choice == 1 :
    func.add_task()
  elif choice == 2 :
    func.view_task()
  elif choice == 3 :
    func.del_task()
  elif choice == 4 :
    exit = input("Enter 'y' To Exit:").lower()
    if exit == 'y':
      break
    else:
      continue
  else:
    print("INVALID INPUT.")