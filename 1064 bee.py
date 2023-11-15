n = 0
m = 0
for i in range (0,6):

    x=float(input())

    if x > 0:
        n+=1
        m+=x

print(f'{n} valores positivos')
print(f'{m/n:.1f}')