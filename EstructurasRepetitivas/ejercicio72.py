G = 6.67259e-11
M = 5.97e24

mayor_fuerza = 0
menor_fuerza = None

mayor_masa = 0
suma_masa = 0

mayor_altura = 0
menor_altura = None

suma_fuerza = 0
contador = 0

nombre = input("Nombre del satélite (fin para terminar): ")

while nombre != "fin":

    pais = input("País: ")
    masa = float(input("Masa (kg): "))
    altura = float(input("Altura (m): "))

    # Calcular fuerza
    fuerza = (G * masa * M) / (altura ** 2)

    # Mayor y menor fuerza
    if contador == 0:
        menor_fuerza = fuerza
        menor_altura = altura
    else:
        if fuerza > mayor_fuerza:
            mayor_fuerza = fuerza
        if fuerza < menor_fuerza:
            menor_fuerza = fuerza

    # Mayor masa
    if masa > mayor_masa:
        mayor_masa = masa

    # Mayor y menor altura
    if altura > mayor_altura:
        mayor_altura = altura
    if menor_altura is None or altura < menor_altura:
        menor_altura = altura

    suma_fuerza += fuerza
    suma_masa += masa
    contador += 1

    nombre = input("Nombre del satélite (fin para terminar): ")

# Promedios
if contador > 0:
    promedio_fuerza = suma_fuerza / contador
    promedio_masa = suma_masa / contador
else:
    promedio_fuerza = 0
    promedio_masa = 0

print("\nMayor fuerza:", mayor_fuerza)
print("Menor fuerza:", menor_fuerza)
print("Fuerza promedio:", promedio_fuerza)

print("\nMayor masa:", mayor_masa)
print("Masa promedio:", promedio_masa)

print("\nMayor altura:", mayor_altura)
print("Menor altura:", menor_altura)