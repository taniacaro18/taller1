total=0
sm=sh=cm=ch=0
sol=cas=otro=0
e1=e2=e3=0
m_ad= h_j=0
hs=ms=0

edad=int(input("Edad (0 salir): "))

while edad!=0:
    sexo=input("Sexo (M/H): ")
    est=int(input("Estado (1 sol,2 cas,3 otro): "))
    esp=int(input("Especialidad (1-3): "))
    
    total+=1
    
    if sexo=="M":
        sm+=edad; cm+=1
        if edad>21: m_ad+=1
        if est==1: ms+=1
    else:
        sh+=edad; ch+=1
        if 17<edad<21: h_j+=1
        if est==1: hs+=1
    
    if est==1: sol+=1
    elif est==2: cas+=1
    else: otro+=1
    
    if esp==1: e1+=1
    if esp==2: e2+=1
    if esp==3: e3+=1
    
    edad=int(input("Edad (0 salir): "))

# RESULTADOS
if cm>0: print("Prom mujeres:", sm/cm)
if ch>0: print("Prom hombres:", sh/ch)

print("Mujeres:", cm)
print("Hombres:", ch)

if total>0:
    print("% solteros:", sol/total*100)
    print("% casados:", cas/total*100)
    print("% otros:", otro/total*100)
    
    print("Esp1:", e1, "%:", e1/total*100)
    print("Esp2:", e2, "%:", e2/total*100)
    print("Esp3:", e3, "%:", e3/total*100)
    
    print("% mujeres adultas:", m_ad/total*100)
    print("% hombres jóvenes:", h_j/total*100)

print("Hombres solteros:", hs)
print("Mujeres solteras:", ms)