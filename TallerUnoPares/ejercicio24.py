capital = float(input("Ingrese la cantidad invertida: "))

tasa = 0.10

interes = capital * tasa

print("Intereses generados:", interes)

if interes > 7000:
    capitalfinal = capital + interes
    print("Los intereses son mayores a 7000, se reinvierten.")
    print("El capital final es:", capitalfinal)
else:
    print("Los intereses son menores o iguales a 7000, no se reinvierten.")
    print("El capital final es:", capital)