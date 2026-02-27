g = int(input("Cantidad de grupos: "))

suma_general_grupos = 0

for i in range(g):

    print("\n--- GRUPO", i+1, "---")
    n = int(input("Cantidad de alumnos en el grupo: "))

    suma_grupo = 0

    for j in range(n):

        print("\nAlumno", j+1)
        m = int(input("Cantidad de materias: "))

        suma_alumno = 0

        for k in range(m):

            print("Materia", k+1)

            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))

            promedio_materia = (nota1 + nota2 + nota3) / 3
            suma_alumno += promedio_materia

        promedio_alumno = suma_alumno / m
        print("Promedio del alumno:", round(promedio_alumno, 2))

        suma_grupo += promedio_alumno

    promedio_grupo = suma_grupo / n
    print("Promedio del grupo:", round(promedio_grupo, 2))

    suma_general_grupos += promedio_grupo

promedio_general = suma_general_grupos / g
print("\nPromedio general de todos los grupos:", round(promedio_general, 2))