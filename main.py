from uuid import uuid1
from datetime import datetime
class Task:

      def __init__(self) -> None:
            self.task=[]
           
      
      def add_task(self,task_name):
            dic={}
            dic["ID"]=uuid1()
            dic["Task" ]=task_name
           
            now = datetime.now()
            dic["Created Time"] = now.strftime("%d/%m/%Y %H:%M:%S") 
            dic["Updated Time"] ="NA"
            dic["Completed"]=False
            dic["Completed Time"] ="NA"
            self.task.append(dic)
            
            
      
      def show_task(self):
            for all in self.task:
                  for item,value in all.items():
                        print(item," - ",value)
                  print("\n")
      
      def show_complete_task(self):
            check =True
            for all in self.task:
                  if all["Completed"] == True:
                          check =False
                          for item,value in all.items():
                                    print(item," - ",value)
                          print("\n")
            if(check ):
                  print("No Taks completed Yet")
                                    
      def show_incomplete_task(self):
            check =True
            for all in self.task:
                  if all["Completed"] == False:
                          check =False
                          for item,value in all.items():
                                    print(item," - ",value)
                          print("\n")
            if(check ):
                  print("No Incomplete Task")
                  
      def update_task(self):
            if(len(self.task) == 0):
                  print("No Task Added")
                  print("\n")
            else:
                 
                  check =True
                  print("Select Which Task To Update")
                  for i in range(len( self.task)):
                        if self.task[i]["Completed"] == False:
                              check =False
                              print("Task No - ",i+1)
                            
                              for item,value in self.task[i].items():
                                    print(item," - ",value)
                        print("\n")
                  if(check):
                        print("No Task To Update")
                        return
                  t_n =int(input("Enter Task No : "))
                  if (t_n>len(self.task)):
                        print("Invalid Input")
                  else:
                        new_t_name=input("Enter New Task : ")
                        t_n-=1
                        for k in range(len(self.task)):
                              if(t_n == k):
                                    self.task[k]["Task"]=new_t_name
                                    now = datetime.now()
                                    self.task[k]["Updated Time"]=now.strftime("%d/%m/%Y %H:%M:%S")
                        
                        print("Task Updated Successfully")
                                     
      def complete_task(self):
            if(len(self.task) == 0):
                  print("No Task Added")
                  print("\n")
            else:
                  
                  check =True
                  print("Select Which Task To Complete")
                  for i  in range(len( self.task)):
                        if self.task[i]["Completed"] == False:
                              check=False
                              print("Task No - ",i+1)
                            
                              for item,value in self.task[i].items():
                                    print(item," - ",value)
                        print("\n")
                  if(check):
                        print("No Task To Complete")
                        return
                  t_n =int(input("Enter Task No : "))
                  if (t_n>len(self.task)):
                        print("Invalid Input")
                  else:
                       
                        t_n-=1
                        for k in range(len(self.task)):
                              if(t_n == k):
                                    self.task[k]["Completed"]=True
                                    now = datetime.now()
                                    self.task[k]["Completed Time"]=now.strftime("%d/%m/%Y %H:%M:%S")
                        
                        print("Task Completed Successfully")
                                     
      
      
                                  
                                    
                  
                  
                  
            
                  
            



task =Task()
while(True):
      print("1 .Add New Task")
      print("2 .Show All Task")
      print("3 .Show Incomplete Task")
      print("4 .Show complete Task")
      print("5 .Update Task")
      print("6 .Mark A  Task Completed")
      
      op =int(input("Enter Option : "))
      
      if (op == 1):
            task_name =input("Enter New Task : ")
            task.add_task(task_name)
            print("Task Created Successfully")
            print("\n")
      elif(op == 2):
            task.show_task()
      elif(op == 3):
            task.show_incomplete_task()
      elif(op == 4):
            task.show_complete_task()
      elif(op == 5):
            task.update_task()
      elif(op == 6):
            task.complete_task()
      else:
            print("Invalid Input")
            
                  
