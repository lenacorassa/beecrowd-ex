n=int(input())
while n:
    n-=1
    nome=input()
    dificuldade=float(input())
    nota=[float(x) for x in input().split()]
    # nota_ordem = nota.sort()
    # nota_ordem = nota_ordem [1:-1]
    soma_notas=sum(nota)-max(nota)-min(nota)
    nota_final=soma_notas*dificuldade
    print(f'{nome} {nota_final:.2f}')