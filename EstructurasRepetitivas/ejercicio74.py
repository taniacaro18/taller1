n_obreros = int(input("Cantidad de obreros: "))

obreros_cumplen = 0
mayor_produccion = 0
nombre_mayor = ""
total_general = 0

for i in range(n_obreros):

    nombre = input("\nNombre obrero: ")
    limite = int(input("Limite semanal: "))

    total_semana = 0

    for dia in range(6):
        produccion = int(input("Produccion del dia: "))
        total_semana += produccion

    porcentaje = (total_semana * 100) / limite

    print("Total semana:", total_semana)
    print("Porcentaje respecto al limite:", porcentaje)

    if total_semana >= limite:
        obreros_cumplen += 1

    if total_semana > mayor_produccion:
        mayor_produccion = total_semana
        nombre_mayor = nombre

    total_general += total_semana

porcentaje_cumplen = (obreros_cumplen * 100) / n_obreros
promedio = total_general / n_obreros

print("\nPorcentaje que cumplieron:", porcentaje_cumplen)
print("Mayor productor:", nombre_mayor, mayor_produccion)
print("Promedio general:", promedio)