M = int(input("Cantidad empleados: "))

total_sueldos = 0
suma_edades = 0
ven1 = ven2 = ven3 = 0
ext_impar = 0

for i in range(M):

    nombre = input("Nombre: ")
    nac = input("Nacionalidad (V/E): ")
    edad = int(input("Edad: "))
    tipo = int(input("Tipo (1,2,3): "))
    horas = int(input("Horas: "))

    if tipo == 1:
        sueldo = horas * 5000
    elif tipo == 2:
        sueldo = horas * 10000
    else:
        sueldo = horas * 15000

    seguro = 0
    if sueldo > 100000:
        seguro = sueldo * 0.03

    print("Sueldo:", sueldo)
    print("Seguro:", seguro)

    total_sueldos += sueldo
    suma_edades += edad

    if nac == "V":
        if tipo == 1:
            ven1 += 1
        elif tipo == 2:
            ven2 += 1
        else:
            ven3 += 1

    if nac == "E" and edad % 2 != 0:
        ext_impar += 1


print("Promedio edad:", suma_edades / M)
print("Venezolanos tipo 1:", ven1)
print("Venezolanos tipo 2:", ven2)
print("Venezolanos tipo 3:", ven3)
print("Extranjeros edad impar:", ext_impar)
print("Total general sueldos:", total_sueldos)