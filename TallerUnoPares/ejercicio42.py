edad = float(input("Ingrese la edad en años (ejemplo 0.5 si es 6 meses): "))
sexo = input("Ingrese el sexo (M/F): ")
hemo = float(input("ngrese nivel de hemoglobina: "))



if edad <= 1/12:  # 1 mes
    if hemo < 13:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

elif edad <= 0.5:  # 6 meses
    if hemo < 10:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

elif edad <= 1:  # 12 meses
    if hemo < 11:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

elif edad <= 5:
    if hemo < 11.5:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

elif edad <= 10:
    if hemo < 12.6:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

elif edad <= 15:
    if hemo < 13:
        print("POSITIVO: Tiene anemia")
    else:
        print("NEGATIVO: No tiene anemia")

else:
    if sexo == "F":
        if hemo < 12:
            print("POSITIVO: Tiene anemia")
        else:
            print("NEGATIVO: No tiene anemia")
    else:
        if hemo < 14:
            print("POSITIVO: Tiene anemia")
        else:
            print("NEGATIVO: No tiene anemia")