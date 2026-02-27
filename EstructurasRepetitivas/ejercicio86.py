nombres = ["Ana","Luis","Pedro","Maria"]
edades = [30,45,25,50]

promedio = sum(edades)/len(edades)

mayor = max(edades)
menor = min(edades)

print("Promedio edad:", promedio)
print("Mayor edad:", mayor)
print("Menor edad:", menor)

mayores_prom = sum(1 for e in edades if e > promedio)
menores_prom = sum(1 for e in edades if e < promedio)

print("Mayores al promedio:", mayores_prom)
print("Menores al promedio:", menores_prom)