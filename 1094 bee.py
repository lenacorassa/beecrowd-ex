n=int(input())
C=0
R=0
S=0
T=0
for i in range(0,n):
    a,b=input().split()
    a=int(a)
    T+=a

    if b=="C":
        C+=a
    elif b=="R":
        R+=a
    elif b=="S":
        S+=a

print(f'''Total: {T} cobaias
Total de coelhos: {C}
Total de ratos: {R}
Total de sapos: {S}''')
print(f'''Percentual de coelhos: {100*C/T:.2f} %
Percentual de ratos: {100*R/T:.2f} %
Percentual de sapos: {100*S/T:.2f} %''')