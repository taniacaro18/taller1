capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa (ejemplo 0.06): "))
semanas = int(input("Ingrese duración en semanas: "))

dias = semanas * 7

for i in range(dias):

    interes = (tasa * capital) / 365
    capital = capital + interes

print("Capital acumulado final:", capital)