def suma_divisores(n):
    suma = 0
    divisor = 1
    
    while divisor < n:
        if n % divisor == 0:
            suma += divisor
        divisor += 1
    
    return suma


contador = 0
numero = 2

while contador < 4:   
    
    sumaA = suma_divisores(numero)
    
    
    if sumaA > numero:
        sumaB = suma_divisores(sumaA)
        
        if sumaB == numero:
            print("Numeros amigos:", numero, "y", sumaA)
            contador += 1
    
    numero += 1