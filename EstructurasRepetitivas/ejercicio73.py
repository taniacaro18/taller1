fecha_dada = input("Ingrese fecha de control (dd/mm/aaaa): ")

n_estados = int(input("Cantidad de estados: "))

total_maximos_agencias = 0
contador_agencias_nacional = 0

for e in range(n_estados):

    cod_estado = input("\nCodigo estado: ")
    n_agencias = int(input("Cantidad de agencias en el estado: "))

    total_estado = 0
    mayor_agencia = None
    menor_agencia = None
    monto_mayor_agencia = 0
    monto_menor_agencia = None

    for a in range(n_agencias):

        cod_agencia = input("\nCodigo agencia: ")
        n_clientes = int(input("Cantidad de clientes: "))

        total_agencia = 0
        clientes_con_deuda = 0
        mayor_deuda_cliente = 0
        cod_cliente_mayor = None

        for c in range(n_clientes):

            cod_cliente = input("\nCodigo cliente: ")
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")
            n_pagares = int(input("Cantidad de pagares: "))

            total_cliente = 0
            pagares_pendientes = 0

            print("\nRECIBO CLIENTE")
            print("Cliente:", cod_cliente, nombre)
            print("Estado:", cod_estado, "Agencia:", cod_agencia)

            for p in range(n_pagares):

                num_pagare = input("Numero pagare: ")
                fecha_venc = input("Fecha vencimiento: ")
                monto = float(input("Monto: "))

                if fecha_venc <= fecha_dada:
                    print("Pagare:", num_pagare,
                          "Fecha:", fecha_venc,
                          "Monto:", monto)

                    total_cliente += monto
                    pagares_pendientes += 1

            if pagares_pendientes > 0:
                clientes_con_deuda += 1
                total_agencia += total_cliente

                print("Total pagares:", pagares_pendientes)
                print("Total deuda cliente:", total_cliente)

                if total_cliente > mayor_deuda_cliente:
                    mayor_deuda_cliente = total_cliente
                    cod_cliente_mayor = cod_cliente

        # RESUMEN POR AGENCIA
        print("\n--- RESUMEN AGENCIA ---")
        print("Codigo agencia:", cod_agencia)
        print("Estado:", cod_estado)
        print("Clientes con deuda:", clientes_con_deuda)
        print("Total adeudado:", total_agencia)
        print("Cliente con mayor deuda:", cod_cliente_mayor)

        total_estado += total_agencia

        # Mayor y menor agencia del estado
        if monto_menor_agencia is None:
            monto_menor_agencia = total_agencia
            menor_agencia = cod_agencia

        if total_agencia > monto_mayor_agencia:
            monto_mayor_agencia = total_agencia
            mayor_agencia = cod_agencia

        if total_agencia < monto_menor_agencia:
            monto_menor_agencia = total_agencia
            menor_agencia = cod_agencia

        total_maximos_agencias += monto_mayor_agencia
        contador_agencias_nacional += 1

    # RESUMEN POR ESTADO
    print("\n=== RESUMEN ESTADO ===")
    print("Codigo estado:", cod_estado)
    print("Total adeudado estado:", total_estado)
    print("Agencia mayor deuda:", mayor_agencia)
    print("Agencia menor deuda:", menor_agencia)

# PROMEDIO NACIONAL
if contador_agencias_nacional > 0:
    promedio_nacional = total_maximos_agencias / contador_agencias_nacional
else:
    promedio_nacional = 0

print("\nPROMEDIO NACIONAL DE MAXIMOS AGENCIAS:", promedio_nacional)