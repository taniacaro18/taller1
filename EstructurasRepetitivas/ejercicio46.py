# ejercicio 46 
N = int(input("Digite N: "))
K = int(input("Digite K: "))

if K < N:
    while N >= K:
        print(N)
        N = N - 1
else:
    print("K debe ser menor que N")