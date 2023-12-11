# a = []
# V = int(input())
# a.append([V*a*2 for x in range(1,10+1)])
# print(a)
# for i in range(len(a)):
#     print('N{0} = {1}'.format(i, a[i]))
a = []
for i in range(10):
    if i == 0:
        v = int(input())
        aux = v
        a.insert(i,v)
    else:
        aux *= 2
        a.insert(i,aux)

for i in range(10):
    print('N[{0}] = {1}'.format(i,a[i]))