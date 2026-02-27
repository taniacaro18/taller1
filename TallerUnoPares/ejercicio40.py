lectura_anterior = float(input("ingrese lectura anterior: "))
lectura_actual = float(input("ingrese lectura actual: "))

consumo = lectura_actual - lectura_anterior



if consumo <= 100:
    monto = consumo * 2.622

elif consumo <= 300:
    monto = consumo * 79.78

elif consumo <= 500:
    monto = consumo * 89.52

else:
    monto = consumo * 97.95

print("consumo en Kwh:", consumo)
print("monto a pagar:", monto, "Bs")