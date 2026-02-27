# ejercicio 32

P = int(input("ingrese el valor de p :"))
Q = int(input("ingrese el valor de q :"))


resultado = (P ** 3) + (Q **4) - (2*(P**2))
if resultado > 680:
    print ("el resultado es mayor a 680")
    print (" P =", P)
    print (" Q =", Q)
    
else:
    print ("el resultado es menor a 680")