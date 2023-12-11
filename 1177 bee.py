# t=int(input())
# v=[]
# l=[]
# for i in range (t-t,t):
#     v.append(i)
# for x in range(0,10):
#     l.append(v)
# print(l)

t = int(input())
n = [] 
for i in range(1000):
    j = 0
    while j < t:
        n.append(j)
        j = j + 1
    print('N[{0}] = {1}'.format(i,n[i]))