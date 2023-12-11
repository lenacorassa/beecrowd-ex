def maxmin(a,b):
    if a>=b:
        return a,b
    else:
        return b,a
n=int(input())
c=0
for i in range (0,n):
    r,s=map(int, input().split())
    r=maxmin(r,s)
    for i in range(r,s):
        if i%2!=0:
                c+=i
        print (c)
    