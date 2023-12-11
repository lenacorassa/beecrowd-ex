a=1
while a>0:
    lista1=list(map(int, input().split()))
    lista1.sort()
    c=0
    a=lista1[0]
    b=lista1[1]
    if a>0:
        while a<=b:
            c+=a
            print(a,end=' ')
            a+=1

        print(f'Sum={c}')