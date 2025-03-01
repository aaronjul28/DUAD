import random

def student_data():
    condition="yes"
    all_students_data=[]
    while condition == "yes":
        student=random.randint(0,1000)
        student={}
        full_name=input("Student's full name: ")
        student_class=input("Enter the student's class: ")
        course_list=["science","english","spanish","history"]
        counter=0
        for i in course_list:
            grade=int(input(f"Enter {i} grade for student {full_name}: "))     
            student['name']=full_name
            student['clase']=student_class       
            student[i]=grade
            
            if grade not in range(100):
                grade=int(input(f"Please enter a valid grade for student {full_name}: "))            
                student[i]=grade
            counter=counter+1
        all_students_data.append(student)
        condition=input("Do you want to add another student?(yes/no): ")
    

    return all_students_data