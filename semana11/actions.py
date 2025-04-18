import random
import json
import random

class Student:
    def __init__(self):
        self.name=input('Enter the name of the Student: ')
        self.classroom=input('Enter the classroom name: ')
        self.science=int(input('Enter the grade for Science: '))
        if self.science not in range(101):
            self.science=int(input('Invalid number, enter a grade from 0-100: '))
        self.spanish=int(input('Enter the grade for Spanish: '))
        if self.spanish not in range(101):
            self.spanish=int(input('Invalid number, enter a grade from 0-100: '))       
        self.english=int(input('Enter the grade for English: '))
        if self.english not in range(101):
            self.english=int(input('Invalid number, enter a grade from 0-100: '))        
        self.history=int(input('Enter the grade for History: '))
        if self.history not in range(101):
            self.history=int(input('Invalid number, enter a grade from 0-100: '))

def student_data():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    condition='yes'
    grades=['name','classroom','science','spanish','english','history']
    full_students_list=[]
    while condition!='no':
        student_dic={}
        student_list=[]
        student=Student()
        student_list.extend((student.name,student.classroom,student.science,student.spanish,student.english,student.history))
        count=0
        for i in grades:
            student_dic[i]=student_list[count]
            count=count+1
        full_students_list.append(student_dic)
        condition=input('Do you want to add a new student?: ')

    with open(file_path,'a') as file:
        data=json.dumps(student_dic)
        file.write(str(data))
        file.write(str('\n'))
            
#right now we are not using the list of dictionaries all_students data

    #return all_students_data

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

