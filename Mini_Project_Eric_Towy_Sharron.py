"""
Eric Chao
Towy windrow
Sharron Chen
Mini_Project_Eric_Towy_Sharron
"""
#==============================================================================
# Lists
courses_available = ["EECE 2140", "MATH 2341", "MATH 2321", "ARCH 1450", "PHYS 1151", "MATH 1342"]
courses_register = []

#==============================================================================
# Functions
def view_courses():
    print("These are all the available courses: ")
    for i in range(len(courses_available)):
        print(i + 1, courses_available[i])  
        
def register_courses():
    print("Please select 3 courses to register for (1-6)")
    for i in range(3):
        student_register = eval(input("What course number would you like register for: "))
        courses_register.append(courses_available[student_register - 1])
        
def display_courses():
    for i in range(3):
        print("course", i + 1, courses_register[i])  
    
#==============================================================================
# Main function
def main():   
    view_courses()
    register_courses()
    user_ask = input("Would you like to see your registered courses (y/n)? ")
    if user_ask == "y":        
        display_courses()
    else:
        print("You're all set! Have a great day and a great semester! ")
    
#==============================================================================

# Invoke the main function
main()
