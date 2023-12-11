n = int(input())
for i in range(n):
    lista= input()

    letra=lista[1]
    alg1=int(lista[2])
    alg2=int(lista[0])

    if (alg1==alg2):
        mult=alg1*alg2
        print(mult)
    
    elif (letra.islower()):
        add=alg1+alg2
        print(add)
    
    elif(letra.isupper()):
        sub=alg1-alg2
        print(sub)
