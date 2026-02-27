dias = 0
suma_max = 0
suma_min = 0
errores = 0
total = 0

max_temp = float(input("Ingrese temperatura maxima: "))
min_temp = float(input("Ingrese temperatura minima: "))

while not (max_temp == 0 and min_temp == 0):

    total += 1

    if 14 <= max_temp <= 30 and 14 <= min_temp <= 30:
        dias += 1
        suma_max += max_temp
        suma_min += min_temp
    else:
        errores += 1

    max_temp = float(input("Ingrese temperatura maxima: "))
    min_temp = float(input("Ingrese temperatura minima: "))

# Promedios
if dias > 0:
    promedio_max = suma_max / dias
    promedio_min = suma_min / dias
else:
    promedio_max = 0
    promedio_min = 0

# errores
if total > 0:
    porcentaje = (errores / total) * 100
else:
    porcentaje = 0

print("Dias validos:", dias)
print("Promedio maxima:", promedio_max)
print("Promedio minima:", promedio_min)
print("Errores:", errores)
print("Porcentaje error:", porcentaje, "%")