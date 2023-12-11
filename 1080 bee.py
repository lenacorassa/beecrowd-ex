a = b =0

for i in range(1,101):

    x = int(input())

    if x > b:
        b = x
        a = i
        
print(b)
print(a)  