n = int(input())
c = 0
for i in range(n):
    C,P = map(int, input().split())
    c += C / P
if c > 1:
    print("FAIL")
else:
    print("OK")