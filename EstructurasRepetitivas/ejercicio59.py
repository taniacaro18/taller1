menor_prog = 20
no_ing = 0
si_ing = 0
aprob_todas = 0
suma_prog = 0
total = 0
rep_mate = 0
pres_mate = 0

nombre = input("Nombre (salir para terminar): ")

while nombre != "salir":

    mate = float(input("Matemática: "))
    prog = float(input("Programación: "))
    ing = float(input("Inglés (-1 si no presentó): "))

    total += 1
    suma_prog += prog

    if prog < menor_prog:
        menor_prog = prog

    if ing == -1:
        no_ing += 1
    else:
        si_ing += 1

    if mate >= 10 and prog >= 10 and ing >= 10:
        aprob_todas += 1

    if mate >= 0:
        pres_mate += 1
        if mate < 10:
            rep_mate += 1

    nombre = input("Nombre (salir para terminar): ")


print("Menor nota Programación:", menor_prog)

if si_ing > 0:
    print("Porcentaje no presentó inglés:",
          (no_ing / si_ing) * 100, "%")

print("Aprobaron todas:", aprob_todas)

if total > 0:
    print("Promedio Programación:", suma_prog / total)

if pres_mate > 0:
    print("Porcentaje reprobaron Matemática:",
          (rep_mate / pres_mate) * 100, "%")