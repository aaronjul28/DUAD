# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.





def enter_operation():

    print('''
Ingrese la operacion que desea realizar:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado         
6. Off
''')
    
    try:
        option=str(input('Enter the operation you want to perform:'))
        valid_options=['1','2','3','4','5','6']
        if option not in valid_options:
            raise ValueError()

        else:
            return option          

    except ValueError as ex:
        print('exception : value entered out of range (1-6)')
        raise ex        

def enter_number():
    try:
        number_entered=int(input('Enter a number: '))

    except ValueError as ex:
        print(ex)
    
    return number_entered

def calculations():
    current_value=enter_number()
    option_selected=enter_operation()
    
    while option_selected != '5' or option_selected != '6':    
        if option_selected=='1':
            current_value= current_value + enter_number()
            print(f'Result is {current_value}')
            option_selected=enter_operation()


        elif option_selected=='2':
            current_value= current_value  - enter_number()
            print(f'Result is {current_value}')
            option_selected=enter_operation()

        elif option_selected=='3':
            current_value= current_value * enter_number()
            print(f'Result is {current_value}')
            option_selected=enter_operation()

        elif option_selected=='4':
            current_value= current_value / enter_number()
            print(f'Result is {current_value}')
            option_selected=enter_operation()

        elif option_selected=='5':
            current_value=0
            print(f'Current value is {current_value}')
            option_selected=enter_operation()

        else:
            exit()

    return current_value, type(option_selected)

def main():
    try:
        calculations()
    except Exception as ex:
        print(ex)


main()