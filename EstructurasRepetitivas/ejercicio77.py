total_pais = 0
mayor_poblacion = 0
menor_poblacion = None
estado_mayor = ""
estado_menor = ""

for i in range(5):

    nombre_estado = input("\nNombre del estado: ")
    m = int(input("Cantidad de municipios: "))

    total_estado = 0

    for j in range(m):
        habitantes = int(input("Habitantes del municipio: "))
        total_estado += habitantes

    print("Total estado:", total_estado)

    total_pais += total_estado

    if i == 0:
        menor_poblacion = total_estado
        estado_menor = nombre_estado

    if total_estado > mayor_poblacion:
        mayor_poblacion = total_estado
        estado_mayor = nombre_estado

    if total_estado < menor_poblacion:
        menor_poblacion = total_estado
        estado_menor = nombre_estado

promedio_estado = total_pais / 5

print("\nEstado mayor población:", estado_mayor, mayor_poblacion)
print("Estado menor población:", estado_menor, menor_poblacion)
print("Promedio por estado:", promedio_estado)
print("Porcentaje respecto al país:", 100, "%")