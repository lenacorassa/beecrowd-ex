x = []
for i in range(10):
    n = int(input())
    if n <= 0:
        n= 1
        x.insert(i,n)
    else:
        x.insert(i,n)

for i in range(10):
    print('X[{0}] = {1}'.format(i,x[i]))