nombre= input("Ingrese su nombre:")
apellido= input("Ingrese su apellido:")
edad= float(input("Ingrese su edad:"))

#BEBE
if (edad <= 1):
    print(f'{nombre} es un bebe.')

#niño
elif (edad <= 5 and edad > 1):
    print(f'{nombre} es un niño.')
    

#PREADOSLESCENTE
elif (edad <= 12 and edad > 5):
    print(f'{nombre} es un adolescente.')

#ADOLESCENTE
elif (edad <= 20 and edad > 12):
    print(f'{nombre} es un adolescente.')

#ADULTO JOVEN
elif (edad <= 44 and edad > 20):
    print(f'{nombre} es un adulto joven.')

#ADULTO 
elif (edad <=60  and edad > 44):
    print(f'{nombre} es un adulto.')

#ADULTO MAYOR
else:
    print(f'{nombre} es un adulto mayor.')