m = int(input())
f1 = int(input())
f2 = int(input())
f3 = m - (f1 + f2)

if f1 > f2 and f1> f3:
    print(f1)
elif f2 > f3 and f2> f1:
    print(f2)
elif f3 > f2 and f3> f1:
    print(f3)