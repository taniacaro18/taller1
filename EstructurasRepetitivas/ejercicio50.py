#Desarrolle un algoritmo o programa que permita calcular y mostrar la suma de todos los números
#pares comprendidos entre 97 y 1003. Respuesta: 249150

suma = 0
for i in range(97,1003):
    if i%2 == 0:
        suma = suma + i
print(suma)