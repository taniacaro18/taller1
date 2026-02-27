extension = [80,60,100]
precio = [500,400,800]

max_precio = max(precio)
pos = precio.index(max_precio)
print("Depto mas costoso:", extension[pos], "m2")

# eliminar
sup = int(input("Superficie a eliminar: "))
if sup in extension:
    pos = extension.index(sup)
    extension.pop(pos)
    precio.pop(pos)