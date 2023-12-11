n=int(input())
c=0
a=0
for i in range(0,n):
    b=int(input())
    if b!=a:
        a=b
        c+=1
print (c)      