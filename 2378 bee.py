leituras,capmax=map(int, input().split())

pessoas=0
cont=0

if 0<leituras<1001 and 0<capmax<1001:
    for x in range (leituras):
        saida,entrada=map(int, input().split())
        pessoas+=entrada-saida
        if pessoas>capmax:
            cont="S"

if cont!="S":
    print("N")
else:
    print(cont)