sueldobase = int(input("Ingrese sueldo base: "))
venta1 = int(input("Ingrese venta 1: "))
venta2 = int(input("Ingrese venta 2: "))
venta3 = int(input("Ingrese venta 3: "))

suma = venta1 + venta2 + venta3

comision = suma * 0.10
neto = sueldobase + comision

print("Sueldo neto:", neto)