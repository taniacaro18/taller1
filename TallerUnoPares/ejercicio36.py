# ejercicio 36

cantidad = int(input("Ingrese la cantidad: "))

if cantidad >= 50000:
    b50000 = cantidad / 50000
    cantidad = cantidad % 50000
    print("Billetes de 50000:", b50000)

if cantidad >= 20000:
    b20000 = cantidad / 20000
    cantidad = cantidad % 20000
    print("Billetes de 20000:", b20000)

if cantidad >= 10000:
    b10000 = cantidad / 10000
    cantidad = cantidad % 10000
    print("Billetes de 10000:", b10000)

if cantidad >= 5000:
    b5000 = cantidad / 5000
    cantidad = cantidad % 5000
    print("Billetes de 5000:", b5000)
    
if cantidad >= 2000:
    b2000 = cantidad / 2000
    cantidad = cantidad % 2000
    print("Billetes de 2000:", b2000)
    
if cantidad >= 1000:
    b1000 = cantidad / 1000
    cantidad = cantidad % 1000
    print("Billetes de 1000:", b1000)
    
if cantidad >= 500:
    b500 = cantidad / 500
    cantidad = cantidad % 500
    print("Billetes de 500:", b500)
    
    
if cantidad >= 100:
    b100 = cantidad / 100
    cantidad = cantidad % 100
    print("Billetes de 100:", b100)
    
if cantidad >= 50:
    b50 = cantidad / 50
    cantidad = cantidad % 50
    print("Billetes de 50:", b50)
    
if cantidad >= 20:
    b20 = cantidad / 20
    cantidad = cantidad % 20
    print("Billetes de 20:", b20)
    
if cantidad >= 10:
    b10 = cantidad / 10
    cantidad = cantidad % 10
    print("Billetes de 10:", b10)