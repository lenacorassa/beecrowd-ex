x=0
m=int(input())
while m>0:  
    x+=1
    print(f"Teste {x}")
    dif=0
    while m>0:
        m-=1
        v1,v2=map(int, input().split())
        dif = v1-v2+dif
        print(dif)
    print()
    m=int(input())