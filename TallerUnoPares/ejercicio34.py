# ejercicio 34

categoria = int(input("ingrese la categoria (1-4) :"))
sueldo = float(input("ingrese el sueldo :"))

if categoria == 1:
    aumento = sueldo * 0.15
elif categoria == 2:
    aumento = sueldo * 0.10
elif categoria == 3:
    aumento = sueldo * 0.08
elif categoria == 4:
    aumento = sueldo * 0.07
else:
    print ("categoria no valida")
    aumento = 0

nuevosueldo = sueldo + aumento


print ("la categoria es", categoria)
print ("el nuevo sueldo es", nuevosueldo)