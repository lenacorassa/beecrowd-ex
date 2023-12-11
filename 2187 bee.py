teste=1
while True:
    n=int(input())
    if n==0:
        break
    b=['0']*4
    if n>=50:
        b[0]=str(n//50)
        n=n%50
    if n>=10:
        b[1]=str(n//10)
        n=n%10
    if n>=5:
        b[2]=str(n//5)
        n=n%5
    b[3]=str(n)
    print(f'Teste {teste}')
    print(' '.join(b))
    print()
    teste+=1








#1
#72
#0
#Teste 1
#0 0 0 1
#Teste 2
#1 2 0 2