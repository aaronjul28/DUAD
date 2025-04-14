import csv
import json
import os


def export_to_csv():
    file_path='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.csv'
    data='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        headers= (
            'name',
            'clase',
            'science',
            'english',
            'spanish',
            'history'
        )
        
        writer = csv.DictWriter(file, headers)
        writer.writeheader()    
        with open(data) as line:
            for i in line.readlines(): 
                data=i
                row=json.loads(data)
                print(f'Exporting data from student {row["name"]}')
                writer.writerow(row)

def import_from_csv():
    file_path=input(
'''
Use this example for reference: /Users/aaronlopez/Documents/PRACTICAS_PYTHON/students2.csv
Enter the path of the file you want to import the data from: ''')
    if file_path =='':
        file_path=input(
'''
You entered an invalid path.
Use this example for reference: /Users/aaronlopez/Documents/PRACTICAS_PYTHON/students2.csv
Enter the path of the file you want to import the data from: ''')
    
    try:
        if os.path.getsize(file_path)==0:
            print('\n!!!CSV file specified is empty!!!')
    except OSError as exception:
        print(f'Error checking file: {exception}')

    data='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.txt'

    with open(file_path,'r') as file:
            dict_reader= csv.DictReader(file,quoting=csv.QUOTE_ALL,quotechar='"')
            for row in dict_reader:
                with open(data,'a') as file_to_write:
                    row=str(row).replace("'",'"')
                    file_to_write.write(row+'\n')



#/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students2.csv
#/Users/aaronlopez/Documents/PRACTICAS_PYTHON/students.csv 