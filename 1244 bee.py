n = int(input())
while n > 0:
    n -= 1
    a = input().split()
    a.sort(key=len, reverse=True)
    for i in range(len(a)):
        print(a[i], end = '')
        if i != len(a)-1:
            print(' ', end = '')
    print()