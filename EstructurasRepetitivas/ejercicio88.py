codigos = [215,102,708]
pagares = [10,15,27]
monto = [50000,30000,25000]

cancelados = []
total_pagado = []

codigo = int(input("Codigo cliente: "))

if codigo in codigos:
    pos = codigos.index(codigo)
    cantidad = int(input("Cantidad a cancelar: "))

    if cantidad <= pagares[pos]:
        pagares[pos] -= cantidad
        cancelados.append(cantidad)
        total_pagado.append(cantidad * monto[pos])

for i in range(len(cancelados)):
    print("Cancelados:", cancelados[i],
          "Total pagado:", total_pagado[i])