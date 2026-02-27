for i in range(5):

    nombre = input("\nNombre de la persona: ")
    peso_anterior = float(input("Peso anterior: "))

    suma_pesos = 0

    for j in range(10):
        peso = float(input("Peso en bascula: "))
        suma_pesos += peso

    promedio = suma_pesos / 10
    diferencia = promedio - peso_anterior

    if diferencia > 0:
        print(nombre, "SUBIO", round(diferencia, 2), "kilos")
    elif diferencia < 0:
        print(nombre, "BAJO", round(abs(diferencia), 2), "kilos")
    else:
        print(nombre, "SE MANTIENE IGUAL")