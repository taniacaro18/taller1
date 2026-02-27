total=agri=min=min_sur=0

trab1=trab2=trab3=trab4=trab5=0
cont1=cont2=cont3=cont4=cont5=0

ind_n=ind_s=ind_e=ind_o=0

act=int(input("Actividad (1-5) o 0 salir: "))

while act!=0:
    loc=int(input("Localización (1-4): "))
    trab=int(input("Trabajadores: "))
    
    total+=1
    
    # Agrícola
    if act==1:
        agri+=1
        trab1+=trab
        cont1+=1
    
    # Industrial
    if act==2:
        trab2+=trab
        cont2+=1
        
        if loc==1: ind_n+=1
        if loc==2: ind_s+=1
        if loc==3: ind_e+=1
        if loc==4: ind_o+=1
    
    # Minera
    if act==3:
        min+=1
        trab3+=trab
        cont3+=1
        if loc==2:
            min_sur+=1
    
    # Pesquera
    if act==4:
        trab4+=trab
        cont4+=1
    
    # Otra
    if act==5:
        trab5+=trab
        cont5+=1
    
    act=int(input("Actividad (1-5) o 0 salir: "))

# Resultados
print("% agrícolas:", (agri/total)*100)

if min>0:
    print("% mineras del sur:", (min_sur/min)*100)

if cont1>0: print("Promedio agrícola:", trab1/cont1)
if cont2>0: print("Promedio industrial:", trab2/cont2)
if cont3>0: print("Promedio minera:", trab3/cont3)
if cont4>0: print("Promedio pesquera:", trab4/cont4)
if cont5>0: print("Promedio otra:", trab5/cont5)

mayor=max(ind_n,ind_s,ind_e,ind_o)

if mayor==ind_n: print("Más industriales en Norte")
elif mayor==ind_s: print("Más industriales en Sur")
elif mayor==ind_e: print("Más industriales en Este")
else: print("Más industriales en Oeste")