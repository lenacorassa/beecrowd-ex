def ehtriangulo(a,b,c):
    n=0
    if a!=b and b!=c and a!=c:
        print("Valido-Escaleno")
        n+=1
    elif (a==b and b!=c) or (a==c and b!=a) or (b==c and a!=c):
        print("Valido-Isoceles")
        n+=1
    elif a==b and b==c:
        print("Valido-Equilatero")
        n+=1
    if n>0:
        if a**2+b**2==c**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")

l1,l2,l3 = sorted(map(int, input().split()))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    ehtriangulo(l1,l2,l3)
else:
    print("Invalido")