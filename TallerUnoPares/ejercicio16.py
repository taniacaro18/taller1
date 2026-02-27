# ejercicio 16

largo = 4
ancho = 1.5
pieza = 0.5

areatotal = largo * ancho

piezastotales = int(areatotal / pieza)

desperdicio = areatotal - (piezastotales * pieza)

print ("el area total de la lamina es de ", areatotal, "metros cuadrados")
print ("el desperdicio es de ", desperdicio, "metros cuadrados")
print ("el numero de piezas es de ", piezastotales)

