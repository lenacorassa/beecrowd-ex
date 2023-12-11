a , b = map(int, input().split())

for i in range(1, b + 1, a):

    for s in range(0,a):

        if s != a - 1:
            print(i, end=' ')
            i += 1
        else:
            print(i)
            i += 1