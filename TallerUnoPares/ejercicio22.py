#ejercicio 22

P = float(input("Ingrese el precio de contado: "))
T = float(input("Ingrese el valor de cada cuota: "))

total = 12 * T
recargo = total - P
porcentaje = (recargo / P) * 100

print("Total pagado en cuotas:", total)
print("Recargo:", recargo)
print("Porcentaje de recargo:", porcentaje, "%")