nombres = ["Maria", "Juan Carlos", "Josefina", "Jose Luis"]

notas = [
    [14,16,15,13,9],
    [10,9,7,11,14],
    [13,12,15,17,13],
    [7,11,10,8,17]
]

promedios = []
suma_clase = 0

for i in range(len(nombres)):
    promedio = sum(notas[i]) / len(notas[i])
    promedios.append(promedio)
    suma_clase += promedio
    print(i+1, nombres[i], round(promedio,2))

promedio_clase = suma_clase / len(nombres)

menor = 0
mayor = 0

for p in promedios:
    if p < promedio_clase:
        menor += 1
    elif p > promedio_clase:
        mayor += 1

print("\nPromedio clase:", round(promedio_clase,2))
print("Menor al promedio:", menor)
print("Mayor al promedio:", mayor)