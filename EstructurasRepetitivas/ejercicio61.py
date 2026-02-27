multiplicador = int(input("Ingrese el primer número: "))
multiplicando = int(input("Ingrese el segundo número: "))

resultado = 0

while multiplicador >= 1:

    print(multiplicador, multiplicando)

    if multiplicador % 2 != 0:
        resultado = resultado + multiplicando

    multiplicador = multiplicador // 2
    multiplicando = multiplicando * 2

print("Resultado:", resultado)