inversion_total = float(input("ingrese la inversión total del negocio: "))
hipoteca = float(input("ingrese el monto de la hipoteca: "))

if hipoteca < 1000000:
    inversion_persona = inversion_total * 0.50
    inversion_socio = inversion_total * 0.50

else:
    inversion_persona = hipoteca
    resto = inversion_total - hipoteca
    inversion_persona = inversion_persona + (resto / 2)
    inversion_socio = resto / 2

print("Inversión de la persona:", inversion_persona)
print("Inversión del socio:", inversion_socio)