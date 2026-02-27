deuda = 12775
pago = 100
incremento = 125

n = 0
pendiente = deuda

print("Pago\tMonto Pago\tSaldo Pendiente")

while pendiente > 0:
    n += 1
    
   
    if pago > pendiente:
        pago = pendiente

    pendiente -= pago

    print(n, "\t", pago, "\t\t", pendiente)

    pago += incremento

print("\nNumero de pagos:", n)
print("Monto del ultimo pago:", pago - incremento)