n = int(input())

for i in range(0,n):
    a = int(input())
    c = 0

    for s in range(1,a):

        if a % s == 0:
            c += s
            
    if a == c:
        print(f'{a} eh perfeito')
    else:
        print(f'{a} nao eh perfeito')