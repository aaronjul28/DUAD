import random
hotel= {
    'habitaciones' :[]
}

hotel['nombre']=input("Ingrese el nombre del Hotel: ")
hotel['estrellas']=input("Ingrese el numero de estrellas del Hotel: ")

conditional=input("Desea agregar informacion acerca de las habitaciones?: ")

while conditional != "no":
    identificador_habitacion= random.randint(0,100)
    identificador_habitacion={}
    identificador_habitacion['numero']=input('Ingrese el numero de la habitacion: ')
    identificador_habitacion['piso']=input('Ingrese el numero de piso: ')
    identificador_habitacion['precio_por_noche']= input('Ingrese el precio por noche: ')
    hotel['habitaciones'].append(identificador_habitacion)
    conditional=input("Desea agregar informacion acerca de las habitaciones?: ")

print(hotel)