"""
Eric Chao
Torrey Winrow
Sharron Chen
Mini_Project_Eric_Torrey_Sharron
"""
#==============================================================================
# Lists
# List of available courses for the user
courses_available = ["EECE 2140", "MATH 2341", "MATH 2321", "ARCH 1450", "PHYS 1151", "MATH 1342"]
# List for courses that the user chooses to register for
courses_register = []

#==============================================================================
# Functions
# Function uses for loop to print all available courses to the user
def view_courses():
    print("These are all the available courses: ")
    for i in range(len(courses_available)):
        print(i + 1, courses_available[i])  

# Function allows user to select 3 courses using for loop
def register_courses():
    print("Please select 3 courses to register for (1-6)")
    for i in range(3):
        student_register = eval(input("What course number would you like register for: "))
        courses_register.append(courses_available[student_register - 1])

# Function to display registered courses to the user by looping through the list of registered courses
def display_courses():
    for i in range(3):
        print("course", i + 1, courses_register[i])  
    
#==============================================================================
# Main function 
def main():   
    view_courses()
    register_courses()
    # Variable to allow the user to see their classes
    user_ask = input("Would you like to see your registered courses (y/n)? ")
    # If-else statement for whether user views their registered courses
    if user_ask == "y":        
        display_courses()
        print("You're all set! Have a great day and a great semester! ")
    else:
        print("You're all set! Have a great day and a great semester! ")
    
#==============================================================================

# Invoke the main function
main()
