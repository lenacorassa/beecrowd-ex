par=0
impar=0
posi=0
neg=0

for i in range (0,5):

    x=int(input())

    if x!=0:
        if x>0:
            posi+=1
        else:
            neg+=1
    if x%2==0:
        par+=1
    else:
        impar+=1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{posi} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')