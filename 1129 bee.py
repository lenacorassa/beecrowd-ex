x = 'ABCDE*'

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(n):
        b = -1
        l = [int(a) for a in input().split()]

        for j in range(len(l)):
            if l[j] <= 127:
                if b != -1:
                    b = 5
                    break
                b = j

        print(x[b])