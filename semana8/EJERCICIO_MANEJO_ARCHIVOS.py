#Cree un programa que lea nombres de canciones de un archivo (línea por línea)
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def file_location():
    file=open('/Users/aaronlopez/Documents/PRACTICAS_PYTHON/MANEJO DE ARCHIVOS/lista_canciones.txt')
    return file    

def make_file_to_list():
    song_file=file_location()
    with song_file as file:
        song_list=file.readlines()
    return song_list

def sort_list():
    list_without_sort=make_file_to_list()
    list_sorted=sorted(list_without_sort)
    return list_sorted

def remove_backslash():
    list_to_remove_backslash=sort_list()
    list_without_backslash=[]
    for i in list_to_remove_backslash:
        song=i
        song_no_spaces=str.rstrip(song)
        list_without_backslash.append(song_no_spaces)
    return list_without_backslash

def save_to_file(file_path):
    file=file_path
    data=remove_backslash()
    with open(file_path,'w') as file:
        for i in data:
            file.write(i)
            file.write("\n")

    
 
def main():
    try:
        file='/Users/aaronlopez/Documents/PRACTICAS_PYTHON/MANEJO DE ARCHIVOS/lista_canciones.txt'
        return save_to_file(file)
    except Exception as ex:
        print(ex)

print(main())