# ejercicio 8

a = float(input("ingrese lado a :"))
b = float(input("ingrese lado b :"))
c = float(input("ingrese lado c :"))

p = (a + b + c) / 2

area = (p * (p - a ) * (p - b) * (p - c)) ** 0.5

print ("el area del triangulo es", area)

