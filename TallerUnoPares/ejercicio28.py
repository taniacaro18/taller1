# ejercicio 28

monto = float(input("ingrese el monto :"))


if monto > 500000:
    propio = monto * 0.55
    banco = monto * 0.30
    credito = monto * 0.15
    
else:
    propio = monto * 0.70
    banco = 0
    credito = monto * 0.30
    

intereses = credito * 0.20

print ("el monto propio es de", propio)
print ("el monto bancario es de", banco)
print ("el monto de credito es de", credito)
print ("el monto de intereses es de", intereses)