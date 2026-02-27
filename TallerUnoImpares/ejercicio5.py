
nombre = input("Ingrese nombre: ")

calificacion1 = float(input("Ingrese calificacion 1: "))
calificacion2 = float(input("Ingrese calificacion 2: "))
calificacion3 = float(input("Ingrese calificacion 3: "))

sumacalifi = calificacion1 + calificacion2 + calificacion3 /3

totalcali = sumacalifi + 0.55

examen = float(input("Ingrese examen: "))

totalexam = examen + 0.30

tabajo = float(input("Ingrese tabajo: "))

totaltab = tabajo + 0.15

totalfinal = totalcali + totalexam + totaltab / 3

print ("El total final es: ", totalfinal)



