nombre = input("Nombre: ")
cedula = input("Cédula: ")
cargo = input("Cargo (obrero/admin/ejecutivo): ")
hijos = int(input("Número de hijos: "))
asistencia = float(input("Porcentaje de asistencia: "))

# Sueldo básico
if cargo == "obrero":
    sueldo = 100000
elif cargo == "admin":
    sueldo = 165500
else:
    sueldo = 250000

# Asignaciones
if hijos > 5:
    hijos = 5

aporte_hijos = sueldo * 0.10 * hijos

aporte_asistencia = 0
if asistencia > 95:
    aporte_asistencia = sueldo * 0.05

# Deducciones
caja = sueldo * 0.10
seguro = sueldo * 0.02

# Sueldo neto
neto = sueldo + aporte_hijos + aporte_asistencia - caja - seguro

# Resultados
print("Nombre:", nombre)
print("Cédula:", cedula)
print("Sueldo básico:", sueldo)
print("Caja de Ahorros:", caja)
print("Seguro Social:", seguro)
print("Sueldo Neto:", neto)