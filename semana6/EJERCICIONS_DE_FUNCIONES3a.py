#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41

def suma_de_valores():
    suma_total=int(0)
    lista_valores=crear_lista_valores()
    for i in lista_valores:
        suma_total=suma_total+i
    return suma_total,lista_valores

def crear_lista_valores():
    condition='yes'
    lista_valores=[]
    while condition == 'yes':
        lista_valores.append(int(input('Ingrese un numero:')))
        condition=input('Quiere agregar mas numeros?: ')
    return lista_valores


def main():
    return suma_de_valores()

print(main())