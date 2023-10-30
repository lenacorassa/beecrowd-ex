n = int(input())
def impar(n):
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(i)
        i += 1

impar(n)