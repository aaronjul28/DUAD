import actions

print("Welcome to the student management tool.")

def menu_options():
    option=int(input("""
    1- Add student information
    2- Review current student information1
    3- Review top 3 students
    4- Review average grades of each student
    5- Export data into a CSV
    6- Import data from a CSV
    7- Exit

Please select one of the following options: """
))
    return option

def option_selected():
    option=menu_options()
    if option == int(1):
        actions.student_data()
        menu_options()    

    if option == int(2):
        print("\n************* Students Information *************\n")
        actions.view_all_students()
        print("\n************************************************\n")
        menu_options()

    if option == int(3):
        print("\n************* Top 3 Students *************\n")
        actions.top_3()
        print("\n************************************************\n")
        menu_options()

print(option_selected())