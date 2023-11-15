def raiz(a, b, z):
    return b + ((b*2-4*a*z)(1/2))/(2*a)
def min(l, h, j, c, k, o):
    if l < h:
        return j*c
    else:
        return h
def max(l, h, j, c):
    if l > h:
        return h
    else:
        return j*c
l, k, c, o, h = map(float, input().split())
j = raiz(c, h+k(c+o), k*l)
print(f'{min(l, h, j, c, k, o):.9f} {max(l, h, j, c):.9f}')