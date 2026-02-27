CT = ["Centro1","Centro2","Centro3"]
H = [50,80,60]  # habitaciones totales
TR = [10,25,15] # restaurantes

# a
max_rest = max(TR)
pos = TR.index(max_rest)
print("Centro con mas restaurantes:", CT[pos])

# b
max_hab = max(H)
pos2 = H.index(max_hab)
print("Centro con mas habitaciones:", CT[pos2])

# c
nombre = input("Ingrese nombre centro: ")
if nombre in CT:
    pos3 = CT.index(nombre)
    print("Habitaciones:", H[pos3])