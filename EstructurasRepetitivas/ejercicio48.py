#ejercicio 48

print("F   C   K   R")

# Rango 1
F = 28
while F <= 54:
    C = 5 * (F - 32) / 9
    R = F + 459.67
    K = C + 273.15
    print(F, C, K, R)
    F = F + 1

# Rango 2
F = 450
while F <= 950:
    C = 5 * (F - 32) / 9
    R = F + 459.67
    K = C + 273.15
    print(F, C, K, R)
    F = F + 50

# Rango 3
F = -50
while F <= 250:
    C = 5 * (F - 32) / 9
    R = F + 459.67
    K = C + 273.15
    print(F, C, K, R)
    F = F + 10