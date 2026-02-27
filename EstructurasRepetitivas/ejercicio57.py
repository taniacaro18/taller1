N = float(input("Ingrese un número positivo: "))

while N <= 0:
    N = float(input("Error. Ingrese un número positivo: "))

X = 0.1

while True:

    RN = (X + N / X) / 2

    if abs(X - RN) < 0.000001:
        break

    X = RN

print("Raíz aproximada:", RN)