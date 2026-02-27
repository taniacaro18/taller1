# ejercicio 14
a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))
d = float(input("Ingrese valor de d: "))
e = float(input("Ingrese valor de e: "))
f = float(input("Ingrese valor de f: "))


denominador = (a * e) - (b * d)


if denominador != 0:
    X = (c * e - b * f) / denominador
    Y = (a * f - c * d) / denominador

    print("El valor de X es:", X)
    print("El valor de Y es:", Y)
else:
    print("no se puede calcular el valor")