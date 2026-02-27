total_promedios = 0

mayor = 0
num_mayor = 0

menor = 5
num_menor = 0

cont_menor3 = 0
cont_mayor4 = 0
cont_45_5 = 0

for i in range(1, 65):

    total_puntos = 0

    for j in range(23):
        nota = int(input("Cuestionario " + str(i) + " pregunta " + str(j+1) + ": "))
        total_puntos += nota

    promedio = total_puntos / 23
    print("Promedio cuestionario", i, ":", promedio)

    total_promedios += promedio

    
    if promedio > mayor:
        mayor = promedio
        num_mayor = i

    
    if promedio < menor:
        menor = promedio
        num_menor = i

    
    if promedio < 3:
        cont_menor3 += 1

    if promedio > 4:
        cont_mayor4 += 1

    if promedio >= 4.5 and promedio <= 5:
        cont_45_5 += 1



prom_general = total_promedios / 64

print("Promedio general:", prom_general)


print("Promedio más alto:", mayor, "Cuestionario:", num_mayor)


print("Promedio más bajo:", menor, "Cuestionario:", num_menor)


if cont_mayor4 > 0:
    porcentaje = (cont_menor3 / cont_mayor4) * 100
    print("Porcentaje menores a 3 respecto a mayores a 4:", porcentaje, "%")


porcentaje_45_5 = (cont_45_5 / 64) * 100
print("Porcentaje entre 4.5 y 5:", porcentaje_45_5, "%")