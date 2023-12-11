n=int(input())
for i in range(0,n):
    a,b,c=map(float, input().split())
    a1=float(a*2)
    b1=float(b*3)
    c1=float(c*5)
    print (f'{(a1+b1+c1)/10:.1f}')