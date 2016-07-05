import time
import pickle
from datetime import date
from datetime import timedelta


class ToDo(object):
    """A ToDo list item. Items have the following properties:

    Attributes:
        name: a string representing the name of the task
        deadline: the deadline of the task
        status: the status of the task
        createdDate: the date that the object or task was created
        associatedTasks: a list of other similar tasks
        Steps to achieve: the steps or subtasks needed to complete the task
        notes: a notes section for - notes
        recurrency: how often the task needs to get done
    """
    # initialize list of items
    toDoList = []


    def __init__(self, name, deadline, status, notes, recurrency):
        """ToDo object constructor """
        self.name = name
        self.deadline = deadline
        self.status = status
        self.createdDate = date.today()
        self.associatedTasks = []
        self.stepsToAchieve = []
        self.notes = notes
        self.recurrency = recurrency

    def show_list():
        print("\n")
        print("#########")
        for i in ToDo.toDoList:
            print(ToDo.toDoList.index(i)+1, i.name, i.deadline, i.status,"\n")
            #"Element was: %r" % i
        print("#########")

    def add_item():
        # may want to rewrite this using vars, or locals to make it a little
        # cleaner and avoid creating an extra array
        print("Okay, let's add a new item to our list")
        inputArray = []
        inputArray.append(input("Enter a name: "))
        print("Enter a date: ")
        deadlineDate = date(x,y,z)
        inputArray.append(input("Enter a deadline: "))
        inputArray.append(input("Enter a status: "))
        inputArray.append(input("Enter any notes: "))
        inputArray.append(input("Enter the recurrency: "))
        newItem = ToDo(inputArray[0], inputArray[1], inputArray[2],
                       inputArray[3], inputArray[4])
        ToDo.toDoList.append(newItem)
        ToDo.show_list()

    def edit_item():
        ToDo.show_list()
        itemChoice = int(input("Which item would you like to edit?: ")) - 1
        #we do minus 1 because of array indexing
        newName = input("Enter a new name for the item: ")
        ToDo.toDoList[itemChoice].name = newName
        #code to edit will go here

    def delete_item():
        ToDo.show_list()
        end = True
        while (end):
            try:
                choice = int(input("Enter a number\n"))
            except ValueError:
                print("Please enter a number from the list\n")
            if choice > len(ToDo.toDoList):
                print("Sorry, that number isn't on the list\n")
            else:
                print("Deleting...")
                #we do minus 1 because of array indexing
                ToDo.toDoList.pop(choice - 1)
                end = False
                             
    def print_whole_list():
        for i in ToDo.toDoList:
            print(i.name, i.deadline, i.status, i.createdDate, i.associatedTasks,
                  i.stepsToAchieve, i.notes, i.recurrency)

    def save_list():
        choice = input("Are you sure you want to save over the old list?")
        if choice == 'y' or "yes":
            pickle.dump(ToDo.toDoList,open("tasks.txt","wb"))
        elif choice == "n" or "no":
            print("Back to the menu")
        else:
            print("No choice selected, back to menu")

    def load_list():
        ToDo.toDoList = pickle.load(open("tasks.txt", "rb"))
        for i in ToDo.toDoList:
            print(ToDo.toDoList.index(i))
        

