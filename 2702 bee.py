def sobras(d,e):
    if d<e:
        return (e-d)
    else:
        return 0
    
o,p,q=map(int, input().split())
a,b,c=map(int, input().split())
r = sobras (o,a) + sobras (p,b) + sobras(q,c)
print(r)
