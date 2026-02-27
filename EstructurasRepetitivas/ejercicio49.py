#ejercicio 49


tres = 0
p1_p2 = 0
p1_p3 = 0
p2_p3 = 0
al_menos_p1 = 0
al_menos_p2 = 0
al_menos_p3 = 0
ninguna = 0

for i in range(100):

    p1 = int(input("Ingrese P1 (1=correcta, 0=incorrecta): "))
    p2 = int(input("Ingrese P2 (1=correcta, 0=incorrecta): "))
    p3 = int(input("Ingrese P3 (1=correcta, 0=incorrecta): "))

    
    if p1 == 1 and p2 == 1 and p3 == 1:
        tres = tres + 1

   
    if p1 == 1 and p2 == 1 and p3 == 0:
        p1_p2 = p1_p2 + 1

   
    if p1 == 1 and p2 == 0 and p3 == 1:
        p1_p3 = p1_p3 + 1

    
    if p1 == 0 and p2 == 1 and p3 == 1:
        p2_p3 = p2_p3 + 1

    
    if p1 == 1:
        al_menos_p1 = al_menos_p1 + 1

    
    if p2 == 1:
        al_menos_p2 = al_menos_p2 + 1

    
    if p3 == 1:
        al_menos_p3 = al_menos_p3 + 1

    
    if p1 == 0 and p2 == 0 and p3 == 0:
        ninguna = ninguna + 1


print("a) Tres correctas:", tres)
print("b) Solo P1 y P2:", p1_p2)
print("c) Solo P1 y P3:", p1_p3)
print("d) Solo P2 y P3:", p2_p3)
print("e) Al menos P1:", al_menos_p1)
print("f) Al menos P2:", al_menos_p2)
print("g) Al menos P3:", al_menos_p3)
print("h) Ninguna correcta:", ninguna)