contador_de_nota = int(1)
cantidad_de_notas_aprobadas = int(0)
cantidad_de_notas_desaprobadas = int(0)
promedio_de_notas_aprobadas = int(0)
promedio_de_notas_desaprobadas = int(0)
promedio_de_notas_total = 0

total_de_notas = int(input("Ingrese la cantidad de notas: "))

while (contador_de_nota <= total_de_notas):
    print(f"Ingrese la nota numero {contador_de_nota}")
    contador_de_nota = contador_de_nota +1
    nota_actual= int(input("Ingrese la nota actual: "))
    if (nota_actual < 70 ):
        cantidad_de_notas_desaprobadas = cantidad_de_notas_desaprobadas+1
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas + nota_actual
        promedio_de_notas_desaprobadas = promedio_de_notas_desaprobadas / cantidad_de_notas_desaprobadas


    else:
        cantidad_de_notas_aprobadas = cantidad_de_notas_aprobadas + 1
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas + nota_actual
        promedio_de_notas_aprobadas = promedio_de_notas_aprobadas / cantidad_de_notas_aprobadas


    promedio_de_notas_total = promedio_de_notas_total + (nota_actual / total_de_notas)


print(f"El estudiante tiene esta cantidad de notas aprobadas: {cantidad_de_notas_aprobadas}")
print(f"Este es el promedio de notas aprobadas: {promedio_de_notas_aprobadas}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {cantidad_de_notas_desaprobadas}")
print(f"Este es el promedio de notas desaprobadas: {promedio_de_notas_desaprobadas}")
print(f"Este es el promedio total de notas: {promedio_de_notas_total}")

