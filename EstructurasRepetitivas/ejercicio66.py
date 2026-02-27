total_pasajeros = 0
no_pagaron = 0

vuelo = int(input("Número de vuelo (0 salir): "))

while vuelo != 0:

    total_vuelo = 0
    
    mayor_peso = 0
    menor_peso = 999999
    
    nombre_mayor = ""
    nombre_menor = ""
    abordo_mayor = ""
    abordo_menor = ""

    pasajero = input("Nombre pasajero (fin para otro vuelo): ")

    while pasajero != "fin":

        abordo = input("Código de abordo: ")
        total_kg = 0
        monto = 0
        
        mayor_maleta = 0
        cod_mayor = ""

        maleta = input("Código maleta (fin para terminar maletas): ")

        while maleta != "fin":

            peso = float(input("Peso maleta: "))
            total_kg += peso

            if peso > mayor_maleta:
                mayor_maleta = peso
                cod_mayor = maleta

            #tarifa
            if peso <= 3:
                monto += 0
            elif peso <= 6:
                monto += 600
            elif peso <= 9:
                monto += 1200
            elif peso <= 12:
                monto += 1500
            elif peso <= 15:
                monto += 2000
            else:
                monto += 2500

            maleta = input("Código maleta (fin para terminar maletas): ")

        # i
        print("Vuelo:", vuelo)
        print("Abordo:", abordo)
        print("Nombre:", pasajero)
        print("Total Kg:", total_kg)
        print("Monto a pagar:", monto)

        # ii
        print("Maleta más pesada:", cod_mayor)

        # iii mayor y menor pasajero
        if total_kg > mayor_peso:
            mayor_peso = total_kg
            nombre_mayor = pasajero
            abordo_mayor = abordo

        if total_kg < menor_peso:
            menor_peso = total_kg
            nombre_menor = pasajero
            abordo_menor = abordo

        total_vuelo += monto

        if monto == 0:
            no_pagaron += 1

        total_pasajeros += 1

        pasajero = input("Nombre pasajero (fin para otro vuelo): ")

    # iii imprimir mayor y menor
    print("Mayor equipaje:", nombre_mayor, mayor_peso)
    print("Menor equipaje:", nombre_menor, menor_peso)

    # iv
    print("Total recaudado vuelo:", total_vuelo)

    vuelo = int(input("Número de vuelo (0 salir): "))

# v
if total_pasajeros > 0:
    print("Porcentaje que no pagaron:",
          (no_pagaron / total_pasajeros) * 100)