#STRING+STRING
print("Hello " + "World")
#PODEMOS CONCATENAR STRINGS SIN PROBLEMA, LOS PONDRA SEGUIDOS EN LA MISMA LINEA

#STRING+INT
#print("Hello " + (1))
print("Hello " + str(1))
#NO SE PUEDE CONCATENAR NUMEROS CON STRINGS A MENOS QUE SE CONVIERTA EL DATA TYPE DEL NUMERO A STRING

#INT+STR
print(str(1)+" uno")
#print(1+" uno")

#NO SE PUEDE CONCATENAR NUMEROS CON STRINGS A MENOS QUE SE CONVIERTA EL DATA TYPE DEL NUMERO A STRING

#LIST+LIST
nombres=["Aaron","David","Carlos"]
apellidos=["Lopez","Brenes","Morales"]
print(nombres+apellidos)

#STR+LIST
nombres=["Aaron","David","Carlos"]
print(nombres[2]+ " is my father")

#FLOAT+INT
weight_one=float(1.35)
weight_two=5
print(weight_one+weight_two)
#EL VALOR DEL RESULTADO SERA EN FLOAT

#BOOL+BOOL
true_value=True
false_value=False

print(true_value+true_value)
print(false_value+false_value)
print(true_value+false_value)
print(false_value+true_value)

#True REPRESENTADO COMO 1 , False REPRESENTADO COMO 0, EL PROGRAMA VA A REALIZAR LA SUMA DE DICHOS VALORES