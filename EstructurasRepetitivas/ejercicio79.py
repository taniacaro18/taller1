PVP1 = 10
PVP2 = 20
PVP3 = 30

n_sucursales = int(input("Cantidad de sucursales: "))
sucursales_cumplen = 0

for s in range(n_sucursales):

    cod_sucursal = int(input("\nCodigo sucursal: "))
    descripcion = input("Descripcion: ")
    venta_esperada = float(input("Venta esperada: "))
    n_puntos = int(input("Cantidad puntos de venta: "))

    total_sucursal = 0
    mayor_comision = 0
    punto_mayor_comision = 0

    for p in range(n_puntos):

        cod_punto = int(input("\nCodigo punto venta: "))

        u1 = int(input("Unidades producto 1: "))
        u2 = int(input("Unidades producto 2: "))
        u3 = int(input("Unidades producto 3: "))

        bruto = (u1*PVP1) + (u2*PVP2) + (u3*PVP3)
        comision = bruto * 0.10
        neto = bruto - comision

        total_sucursal += bruto

        if comision > mayor_comision:
            mayor_comision = comision
            punto_mayor_comision = cod_punto

        print("Punto:", cod_punto)
        print("Bruto:", bruto)
        print("Comision:", comision)

    porcentaje = (total_sucursal * 100) / venta_esperada

    if total_sucursal >= venta_esperada:
        sucursales_cumplen += 1

    print("\nSucursal:", cod_sucursal)
    print("Total vendido:", total_sucursal)
    print("Porcentaje logrado:", porcentaje)
    print("Punto mayor comision:", punto_mayor_comision)

print("\n% sucursales que cumplieron:",
      (sucursales_cumplen*100)/n_sucursales)