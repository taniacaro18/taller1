primer = 6
razon = 5
termino = primer
suma = 0
a12 = 0

for i in range(1, 13):
    
    if i == 12:
        a12 = termino
    
    suma = suma + termino
    termino = termino + razon

print("Termino 12:", a12)
print("Suma de los 12 primeros:", suma)