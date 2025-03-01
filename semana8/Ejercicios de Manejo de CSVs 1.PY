#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB
import random
import csv

def game_info():
    condition=input('Do you want to add information about a game?: ')
    list_of_games=[]
    while condition!='no':
        diccionario_juego= random.randint(0,100)
        diccionario_juego={}
        diccionario_juego['Nombre']=input('Ingrese el nombre del Juego: ')
        diccionario_juego['Género']=input('Ingrese el Género del Juego: ')
        diccionario_juego['Desarrollador']=input('Ingrese el Desarrollador del Juego: ')
        diccionario_juego['Clasificación']=input('Ingrese la Clasificación ESRB: ')
        list_of_games.append(diccionario_juego)
        condition=input('Do you want to add information about a game?: ')

    return list_of_games

def create_csv(file_path):
    with open(file_path,'w',encoding='utf-8') as file:
        data=game_info()
        headers=data[0].keys()
        writer=csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_path):
    with open(file_path) as file:
        reader=csv.DictReader(file)
        for row in reader:
            print(row)

def main():
    path='/Users/aaronlopez/Desktop/PRACTICAS_PYTHON/Ejercicios de Manejo de CSVs/lista_juegos.csv'
    create_csv(path)
    return print(read_csv(path))

main()

