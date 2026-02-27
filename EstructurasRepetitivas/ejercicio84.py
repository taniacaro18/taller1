proveedores = ["Ana","Carlos","Luis"]
ciudades = ["Bogota","Cali","Medellin"]
articulos = [50,80,30]

# a
nombre = input("Proveedor: ")
if nombre in proveedores:
    pos = proveedores.index(nombre)
    print("Ciudad:", ciudades[pos])

# b
nombre = input("Proveedor a actualizar: ")
if nombre in proveedores:
    pos = proveedores.index(nombre)
    nueva = input("Nueva ciudad: ")
    ciudades[pos] = nueva

# c
nombre = input("Proveedor para actualizar articulos: ")
if nombre in proveedores:
    pos = proveedores.index(nombre)
    nuevo = int(input("Nuevo numero articulos: "))
    articulos[pos] = nuevo