import csv
import json


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

