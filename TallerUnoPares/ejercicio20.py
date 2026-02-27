# ejercicio 20

capital = float(input("ingrese el capital prestado :"))
interes = float(input("ingrese los intereses :"))

tiempo = 4

pagado  = (interes * 100) / (capital * tiempo)

print ("el pago anual es de", pagado, "%")
