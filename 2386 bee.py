A=int(input())
N=int(input())

cont=0

while N:
    N-=1
    F=int(input())
    estrela=F*A
    if estrela>=40000000:
        cont+=1

print(cont)