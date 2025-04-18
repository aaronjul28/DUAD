# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.

import json

def open_file(file_path):
    with open(file_path) as file:
        return file.read()

def ask_for_new_information():
    pokemon_dictionary={}
    name=input("What is the Pokemons name: ")
    pokemon_dictionary['name']=name
    type=[input('Whats the Pokemons type: ')]
    pokemon_dictionary['type']=type
    list_of_capabilities={'HP':input("Enter the HP: "),
                          'Attack': input('Enter the attack: '),
                          'Defense':input('Enter the defense: '),
                          'Sp.Attack': input('Enter the Sp Attack:'),
                          'Sp.Deffense': input('Enter the Sp Defense: '),
                          'Speed':input('Enter the Speed: ')}
    pokemon_dictionary['Base']=list_of_capabilities

    return pokemon_dictionary

def append_to_file():
    file_path="/Users/aaronlopez/Documents/PRACTICAS_PYTHON/Ejercicios de Manejo de JSON/POKEMONS.txt"
    data=ask_for_new_information()
    data=json.dumps(data,indent=2)
    with open(file_path,'a') as file:
        file.write(data)

def main():
    try:
        condition=input('Do you want to enter a Pokemon info?: ')
        while condition!='no':
            append_to_file()
            condition=input('Do you want to enter a Pokemon info?: ')
    except Exception as ex:
        print(ex)

main()