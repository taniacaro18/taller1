# ejercicio 26

A = int(input("ingrese el numero de a :"))
B = int(input("ingrese el numero de b :"))
C = int(input("ingrese el numero de c :"))
D = int(input("ingrese el numero de d :"))

if D == 0:
    resultado = (A - C) ** 2
    print ("el resultado es :", resultado)
    
elif D > 0:
    resultado = (A - B) **3
    print ("el resultado es :", resultado)
    
    
else:
    print ("no hay peracion definida")