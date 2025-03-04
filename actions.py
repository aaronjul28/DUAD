import random
import json

def student_data():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
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
        with open(file_path,'a') as file:
            data=json.dumps(student)
            file.write(str(data)+'\n')
#right now we are not using the list of dictionaries all_students data

    return all_students_data

#student_data()

def view_all_students():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    with open(file_path) as file:
        for line in file.readlines():
            data= json.loads(line)
            print(data)
        
