"""
ToDo_List_Chao
Eric Chao
"""

# Creating list so we can hold the task in the todo list
task_list = ["Do 2140 homework", "Study for physics"]

#==============================================================================

# Function to allow the user to veiw the list
def user_veiw():
    for i in range(len(task_list)):
        
        # Printing the list with a for loop so we can print the task number of value in the list
        print("Task", i + 1, "is", task_list[i])

#==============================================================================

def add_list():
    # Asking them for a task to add to the list
    add_list = input("What task do you want to add? ")
    # Adding to the list
    task_list.append(add_list)
    
    # Printing the new list of tasks
    print("Your new list of task are: ")
    for i in range(len(task_list)):
        print("Task", i + 1, "is", task_list[i])

#==============================================================================
        
def delete_list():
    # Printing current task so the user can pick which task to remove
    print("This is your current list of task")
    for i in range(len(task_list)):
        print("Task", i + 1, "is", task_list[i])
        
    # Deleting the task from the list
    delete_task = eval(input("Which task do you want to delete (pleae give the number value): "))
    list_value = delete_task - 1
    task_list.pop(list_value)
    
    # Printing new list of tasks
    print("Your new list of task are: ")
    for i in range(len(task_list)):
        print("Task", i + 1, "is", task_list[i])

#==============================================================================

def main():   
    # Presetting to yes for the while loop
    end_repeat = "y"
    while end_repeat == "y":
        # does user want to look at their task? 
        user_ask = input("Do you want to look at your task? (Use y/n): ")
        if user_ask == "y": 
            user_veiw()
        else:
            # Does the user want to add to list of tasks?
            user_add = input("Do you want to add new tasks? (Use y/n): ")
            if user_add == "y": 
                add_list()
            else:
                # Does the user want to delete from their list of tasks?
                user_delete = input("Do you want to delete one of your task? (y/n): ")
                if user_delete == "y":
                    delete_list()
        
        # Asking the user if they want to reveiw or edit the list still
        end_repeat = input("Do you want to continue or is that it? (y/n)? ")
#==============================================================================

# Invoke the main function
if __name__ == "__main__":
    main()
