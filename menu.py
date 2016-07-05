from ToDo import ToDo
import pickle

class Menu:

    """ declare end variable as class variable, so we can exit an inner loop
    and get back to the main one using methods, avoiding too many nests?
    """
    
    #end = True this might not even be necessary
    

    def display_menu():
        end = True
        while (end):
            print("What would you like to do?\n")
            print("1. See tasks\n")
            print("2. Add task\n")
            print("3. Remove task\n")
            print("4. Edit a task\n")
            print("5. Save your list\n")
            print("6. Load the list\n")
            print("7. Show deadlines\n")
            print("0. Exit the program\n")
            try:
                choice = int(input("Enter a number: "))
            except ValueError:
                print("Please enter a number\n")

            if choice == 1:
                ToDo.show_list()
                #print(toDoList)
        

            elif choice == 2:
                print("Okay, you can add a task\n")
                ToDo.add_item()

            elif choice == 3:
                #print("Okay, you can delete a task\n")
                ToDo.delete_item()

            elif choice == 4:
                #print("Okay, you can edit a task\n")
                
                ToDo.edit_item()

            elif choice == 5:                
                ToDo.save_list()

            elif choice == 6:
                print("Loading the list\n")
                ToDo.load_list()

            elif choice == 7:
                print("Showing deadlines\n")

            elif choice == 0:
                print("See ya later\n")
                end = False

            else:
                print("Please enter a choice from the menu\n")

    def display_std_menu(menuType):
        """This method will take a name as a parameter, so we can call
    the same generic list but use the name as an identifier ie:
    number, if the options are numbers based. we could have the list of
    choices be dynamic. potnetial here epsecially if going to be very
    menus based
    """

 

    def display_menu_cats():
        """ This will be a higher level menu that has more
    general categories (cats) and pull down into subcategories,
    just so that the original list does not get too crowded
    """
        end = True
        while(end):
            print("What would you like to do?\n")
            print("1. View items\n")
            print("2. Interact with task (add, remove, edit)\n")
            print("3. Save the list\n")
            print("4. Load the list\n")
            print("0. Exit the program\n")

            try:
                choice = int(input("Enter a number: "))
            except ValueError:
                print("Please enter a number\n")

            if choice == 1:
                Menu.display_Items_Menu()
                #print(toDoList)
                """ i want this to have the options to view All items,
    view all by deadline, view deadlines, view by status, etc
    """
            elif choice == 2:
                #show interact menu
                Menu.display_Interact_Menu()

            elif choice == 3:
                #save the list
                ToDo.save_list()

            elif choice == 4:
                #load the list
                print("Loading the list\n")
                ToDo.load_list()

            elif choice == 0:
                print("See ya later\n")
                end = False

            else:
                print("Please enter a choice from the menu\n")


    def display_Interact_Menu:
        subEnd = True
        while(subEnd):
            print("What would you like to do?\n")
            print("1. Add an item\n")
            print("2. Delete an item\n")
            print("3. Edit an item\n")
            print("4. Display the list\n")
            print("0. Go back\n")

            try:
                choice = int(input("Enter a number: "))
            except ValueError:
                print("Please enter a number\n")

            if choice == 1:
                ToDo.show_list()
                #print(toDoList)

            elif choice == 2:
                #delete item code

            elif choice == 3:
                #edit item code

            elif choice == 4:
                #display the list

            elif choice == 0:
                subEnd = False

    def display_Items_Menu:
        subEnd = True
        while(subEnd):
            print("What would you like to do?\n")
            print("1. View all items\n")
            print("2. View items by status\n")
            print("3. View items by deadline\n")
            print("4. View items alphabetically\n")
            print("5. View items in created order\n")
            print("6. View items by importance\n")
            print("0. Go back
                
        
                
    
    

