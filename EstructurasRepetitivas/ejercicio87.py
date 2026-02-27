espectaculos = ["A","B","C"]
costos = [1000,1500,1200]
ingresos = [2000,3000,1800]
asistentes = [100,150,120]

ganancias = []

for i in range(len(espectaculos)):
    ganancia = ingresos[i] - costos[i]
    ganancias.append(ganancia)

max_g = max(ganancias)
pos = ganancias.index(max_g)

print("Espectaculo mayor ganancia:", espectaculos[pos])