fib=[0,1]
a=0
b=1

for i in range(60):
    
    total=b+a
    fib.append(total)
    a=b
    b=total

n= int(input())

for i in range(n):
    N=int(input())
    print('Fib(%d) = %d'%(N, fib[N]))