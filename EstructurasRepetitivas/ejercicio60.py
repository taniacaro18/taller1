num = input("Número de factura: ")
cliente = input("Nombre del cliente: ")
monto = float(input("Monto de la factura: "))
dias = int(input("Días que tardó en pagar: "))

interes = 0
descuento = 0

if dias >= 60:
    interes = monto * 0.08

elif dias >= 31 and dias <= 59:
    interes = monto * 0.06

elif dias < 15:
    descuento = monto * 0.02

monto_final = monto + interes - descuento

print("Número factura:", num)
print("Cliente:", cliente)
print("Monto original:", monto)
print("Interés:", interes)
print("Descuento:", descuento)
print("Monto a pagar:", monto_final)