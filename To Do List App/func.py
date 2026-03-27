task = [] #empty list of task
def add_task(): #adds a task
   tsk = input("Please Enter A Task: ")
   task.append(tsk)

def view_task(): #shows tasks
   print("Your Tasks :")
   for item in task:
     print(item)
   print("")

def del_task(): #deletes a task
   del_obj = input("Enter A Task To Delete: ")
   if del_obj in task:
     task.remove(del_obj)
     print("Task Have Been Removed.")
   else:
      print("Sorry Could Not Find The Specific Task")