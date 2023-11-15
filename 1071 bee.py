#x=int(input())
#y=int(input())
#ans=0
#for n in range((y+1),x):
#    if (n%2!=0):
#        ans+=n
#print(ans)

import sys
sys.setrecursionlimit(100000)

def soma(a, b):
    if b%2==0 and b+2<a:
        return b+1+soma(a, b+2)
    elif b%2!=0 and b+2<a:
        return b+2+soma(a, b+2)
    else:
        return 0
x = int(input())
y = int(input())
print(soma(x, y))