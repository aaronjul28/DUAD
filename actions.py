import random
import json
import random

def student_data():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    condition="yes"
    all_students_data=[]
    while condition == "yes":
        student=random.randint(0,1000)
        student={}
        full_name=input("Student's full name: ")
        while full_name == '':
            full_name=input("Please enter a valid name: ")
        student_class=input("Enter the student's class: ")
        while student_class == '':
            student_class=input("Please enter a valid Student Class: ")
        course_list=["science","english","spanish","history"]
        for i in course_list:
            grade=int(input(f"Enter {i} grade for student {full_name}: "))
            student['name']=full_name
            student['clase']=student_class       
            student[i]=grade
            
            if grade not in range(100):
                grade=int(input(f"Please enter a valid grade for student {full_name}: "))            
                student[i]=grade
        all_students_data.append(student)
        condition=input("Do you want to add another student?(yes/no): ")
        with open(file_path,'a') as file:
            data=json.dumps(student)
            file.write(str(data))
            file.write(str('\n'))
            
#right now we are not using the list of dictionaries all_students data

    return all_students_data

#student_data()

def view_all_students():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    with open(file_path) as file:
        for line in file.readlines():
            data= json.loads(line)
            print(data)
        
def top_3():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    all_students_average={}
    count=0
    with open(file_path) as file:
        for line in file.readlines():
            data=json.loads(line)
            name=data["name"]
            average=int(int(data["science"])+int(data["english"])+int(data["spanish"])+int(data["history"]))/4
            all_students_average[name]=average
            count=count+1
    sorted_average=sorted(all_students_average.items(), key=lambda x:x[1], reverse=True)   
    if count < 3:
        for i in sorted_average:
            print(i)
    else:    
        for i in range(3):
            print(sorted_average[i])


# def average():
#     file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
#     all_students_average={}
#     with open(file_path) as file:
#         for line in file.readlines():
#             data=json.loads(line)
#             name=data["name"]
#             average=int(int(data["science"])+int(data["english"])+int(data["spanish"])+int(data["history"]))/4
#             all_students_average[name]=average
#     for i in all_students_average:
#         print(f"{i}:{all_students_average[i]}")

def average():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    with open(file_path) as file:
        
#SCIENCE
        science_grades=[]
        english_grades=[]
        spanish_grades=[]
        history_grades=[]
        
        for line in file.readlines():
            data=json.loads(line)
            science_grades.append(int(data['science']))
            english_grades.append(int(data['english']))
            spanish_grades.append(int(data['spanish']))
            history_grades.append(int(data['english']))

        science_average=0
        english_average=0
        spanish_average=0
        history_average=0

        for i in science_grades:
            science_average=science_average+i
        science_average=science_average/len(science_grades)
        print('Science: ',science_average)

        for i in english_grades:
            english_average=english_average+i
        english_average=english_average/len(english_grades)
        print('English: ',english_average)

        for i in spanish_grades:
            spanish_average=spanish_average+i
        spanish_average=spanish_average/len(spanish_grades)
        print('Spanish: ',spanish_average)

        for i in history_grades:
            history_average=history_average+i
        history_average=history_average/len(history_grades)
        print('history: ',history_average)       


#ENGLISH

