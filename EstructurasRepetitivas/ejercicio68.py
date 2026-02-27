contador_perfectos = 0
numero = 2

while contador_perfectos < 3:
    
    suma = 0
    
   
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            suma += divisor
        divisor += 1
    
   
    if suma == numero:
        print("Numero perfecto:", numero)
        contador_perfectos += 1
    
    numero += 1