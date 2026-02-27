# ejercicio 12

examenmatematicas = float (input("ingrese la nota del examen de matematicas :"))

tareamat1 = float (input("ingrese la nota de la tarea 1 :"))
tareamat2 = float (input("ingrese la nota de la tarea 2 :"))
tareamat3 = float (input("ingrese la nota de la tarea 3 :"))

promediotareamat = (tareamat1 + tareamat2 + tareamat3) / 3

promediomate = (examenmatematicas * 0.90) + (promediotareamat * 0.10)

print (" la nota promedio de la materia es ", promediomate)

print ("-----------------------------------------")

examenfisica = float (input("ingrese la nota del examen de fisica :"))

tareafisica1 = float (input("ingrese la nota de la tarea 1 :"))
tareafisica2 = float (input("ingrese la nota de la tarea 2 :"))


promediotareafisica = (tareafisica1 + tareafisica2 ) / 2

promediofisica = (examenfisica * 0.80) + (promediotareafisica * 0.20)

print (" la nota promedio de la materia es ", promediofisica)

print ("-----------------------------------------")

examenquimica = float (input("ingrese la nota del examen de quimica :"))

tareaquimica1 = float (input("ingrese la nota de la tarea 1 :"))
tareaquimica2 = float (input("ingrese la nota de la tarea 2 :"))
tareaquimica3 = float (input("ingrese la nota de la tarea 3 :"))

promediotareaquimica = (tareaquimica1 + tareaquimica2 + tareaquimica3) / 3

promedioquimica = (examenquimica * 0.85) + (promediotareaquimica * 0.15)

print (" la nota promedio de la materia es ", promedioquimica)

print ("-----------------------------------------")

promediogeneral = (promediofisica + promediomate + promedioquimica) / 3

print (" la nota promedio general es ", promediogeneral)
