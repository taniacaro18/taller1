n_estados = int(input("Cantidad estados: "))

for e in range(n_estados):

    cod_estado = input("\nCodigo estado: ")
    nombre_estado = input("Nombre estado: ")
    n_ciudades = int(input("Cantidad ciudades: "))

    for c in range(n_ciudades):

        cod_ciudad = input("\nCodigo ciudad: ")
        nombre_ciudad = input("Nombre ciudad: ")
        esperado = float(input("Unidades esperadas: "))
        n_canales = int(input("Cantidad canales: "))

        total_unidades = 0
        total_bruto = 0
        com_tienda = 0
        com_calle = 0

        for ca in range(n_canales):

            cod_canal = input("Codigo canal: ")
            n_vendedores = int(input("Cantidad vendedores: "))

            for v in range(n_vendedores):

                cod_vendedor = input("Codigo vendedor: ")
                unidades = int(input("Unidades vendidas: "))
                monto = float(input("Monto total: "))

                total_unidades += unidades
                total_bruto += monto

                if cod_vendedor.startswith("11"):
                    com_tienda += monto * 0.10
                elif cod_vendedor.startswith("12"):
                    com_calle += monto * 0.15

        print("\nCiudad:", cod_ciudad)
        print("Total unidades:", total_unidades)
        print("Bruto:", total_bruto)
        print("Comision tienda:", com_tienda)
        print("Comision calle:", com_calle)