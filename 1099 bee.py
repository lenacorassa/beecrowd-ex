n = int(input())

for i in range(0,n):
    lista = list(map(int, input().split()))
    lista.sort()
    r = lista[0]
    s = lista[1]
    c = 0

    if r == s:
        print(0)

    else:
        while s > r:
            if s % 2 != 0:
                c+= s
                s -= 2 
            
            else:
                c+= s
                s-= 1
                
        print(c - lista[1])