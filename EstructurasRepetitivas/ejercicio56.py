dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    cociente = cociente + 1
    print("Resta:", dividendo)

print("Cociente:", cociente)
print("Resto:", dividendo)