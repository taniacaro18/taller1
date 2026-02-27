total = 0
tachira = 0
distrito = 0

grupo1 = 0
grupo2 = 0
grupo3 = 0
grupo4 = 0

ninos = 0
ninas = 0

nombre = input("Nombre del orfanatorio (fin para terminar): ")

while nombre != "fin":
    
    sexo = input("Sexo (M/F): ")
    edad = int(input("Edad: "))
    estado = input("Estado: ")

    total += 1

    # Contar estados
    if estado == "Tachira":
        tachira += 1
    if estado == "Distrito Capital":
        distrito += 1

    # Grupos de edad
    if edad < 1:
        grupo1 += 1
    elif edad <= 3:
        grupo2 += 1
    elif edad <= 6:
        grupo3 += 1
    else:
        grupo4 += 1

    # Contar sexo
    if sexo == "M":
        ninos += 1
    else:
        ninas += 1

    nombre = input("Nombre del orfanatorio (fin para terminar): ")

# Porcentajes
if total > 0:
    porc_tachira = (tachira / total) * 100
    porc_distrito = (distrito / total) * 100
    porc_ninos = (ninos / total) * 100
    porc_ninas = (ninas / total) * 100
else:
    porc_tachira = porc_distrito = porc_ninos = porc_ninas = 0

print("\nTotal huérfanos:", total)
print("Porcentaje Táchira:", porc_tachira, "%")
print("Porcentaje Distrito Capital:", porc_distrito, "%")

print("\nGrupo 1 (<1 año):", grupo1)
print("Grupo 2 (1-3 años):", grupo2)
print("Grupo 3 (4-6 años):", grupo3)
print("Grupo 4 (>6 años):", grupo4)

print("\nNiños:", ninos, "-", porc_ninos, "%")
print("Niñas:", ninas, "-", porc_ninas, "%")