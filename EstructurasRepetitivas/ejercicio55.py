suma = 0
k = 1
contador = 0

termino = (k**2 + 1) / k

while suma + termino <= 1000:

    suma = suma + termino
    contador = contador + 1

    k = k + 1
    termino = (k**2 + 1) / k


print("Número de términos:", contador)
print("Suma obtenida:", suma)