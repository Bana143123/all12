class ToDoList:
    def __init__(self):
        self.task=[]
    def addtask(self,des):
        self.task.append(des)

    def viewtask(self):
        if not self.task:
            print("There Is No Task Present In Tasks List")
        else:
            print(self.task)
    def removetask(self,ind):
        x={}
        for index,task in enumerate(self.task):
            x.update({index:task})
            #print(type(index))
        print(x)
        print()
        print(ind)
        print()
        print(type(x.keys()))
        if ind in x.keys():
            print(ind)
            y=x[ind]
            print(y)
            print(type(y))
            self.task.remove(y)
        else:
            print("You entered wrong index which is not present inside tasks")
    

        
def menu():
    print("\nToDo-List Manager")
    print("1.Adding tasks")
    print("2.View Tasks")
    print("3.Remove Tasks")
    print("4.Exit")


if __name__=="__main__":
    todolist=ToDoList()
    while True:
        menu()
        choice=input("Enter your choice :")
        if choice == "1":
            Add_your_task=input("Enter your Task Here :")
            todolist.addtask(Add_your_task)
        elif choice== "2":
            todolist.viewtask()
        elif choice== "3":
            ind=int(input("Enter the index you want to remove :"))
            todolist.removetask(ind)
        elif choice=="4":
            print()
            print("Bye Tata CU")
            break
        else:
            print()
            print("You Entered Wrong Choice, Please Cross Check Menu And Enter.")
        