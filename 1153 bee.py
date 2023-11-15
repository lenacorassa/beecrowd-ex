def fatorial(n):
    f=1
    for i in range(0,n):
        f=f*(n-i)
    print(f)    

n=int(input())
fatorial(n)