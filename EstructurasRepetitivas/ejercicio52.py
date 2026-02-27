suma_ninos = 0
suma_jovenes = 0
suma_adultos = 0
suma_viejos = 0

cont_ninos = 0
cont_jovenes = 0
cont_adultos = 0
cont_viejos = 0

for i in range(100):

    edad = int(input("Ingrese edad: "))
    peso = float(input("Ingrese peso: "))

    if edad >= 0 and edad <= 12:
        suma_ninos = suma_ninos + peso
        cont_ninos = cont_ninos + 1

    elif edad >= 13 and edad <= 29:
        suma_jovenes = suma_jovenes + peso
        cont_jovenes = cont_jovenes + 1

    elif edad >= 30 and edad <= 59:
        suma_adultos = suma_adultos + peso
        cont_adultos = cont_adultos + 1

    else:
        suma_viejos = suma_viejos + peso
        cont_viejos = cont_viejos + 1


if cont_ninos > 0:
    print("Promedio niños:", suma_ninos / cont_ninos)

if cont_jovenes > 0:
    print("Promedio jóvenes:", suma_jovenes / cont_jovenes)

if cont_adultos > 0:
    print("Promedio adultos:", suma_adultos / cont_adultos)

if cont_viejos > 0:
    print("Promedio viejos:", suma_viejos / cont_viejos)