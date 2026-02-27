suma = 0
termino = 1
contador = 0

while suma + termino <= 1.99:
    
    suma += termino
    contador += 1
    termino = termino / 2

print("Número de términos:", contador)
print("Suma obtenida:", suma)