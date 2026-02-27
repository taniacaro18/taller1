n_estados = int(input("Cantidad estados: "))

mayor_porcentaje = 0
estado_mayor = ""

for e in range(n_estados):

    cod_estado = input("\nCodigo estado: ")
    n_ciudades = int(input("Cantidad ciudades: "))

    profesionales_desempleados = 0
    total_profesionales = 0

    for c in range(n_ciudades):

        cod_ciudad = input("Codigo ciudad: ")
        n_municipios = int(input("Cantidad municipios: "))

        for m in range(n_municipios):

            cod_municipio = input("Codigo municipio: ")
            n_personas = int(input("Cantidad personas: "))

            contador_condicion = 0

            for p in range(n_personas):

                edad = int(input("Edad: "))
                nivel = input("Nivel (N,B,S,P): ")
                situacion = input("Situacion (D,E): ")

                if edad > 25 and nivel == "N" and situacion == "D":
                    contador_condicion += 1

                if nivel == "P":
                    total_profesionales += 1
                    if situacion == "D":
                        profesionales_desempleados += 1

            print("Municipio:", cod_municipio,
                  "Cantidad condicion:", contador_condicion)

    if total_profesionales > 0:
        porcentaje = (profesionales_desempleados*100)/total_profesionales
        if porcentaje > mayor_porcentaje:
            mayor_porcentaje = porcentaje
            estado_mayor = cod_estado

print("Estado mayor % profesionales desempleados:", estado_mayor)