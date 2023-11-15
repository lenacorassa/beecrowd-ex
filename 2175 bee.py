#def amigos(n):
#    saida = "Otavio"
#    max = n[0] #defini como max o primeiro elemento da lista
#    if n[1] < max: #segundo elemento comparando com o que defini como max
#        saida = "Bruno"
#        max = n[1] #"tornando" mas o seg elem caso ele seja maior
#    if n[2] < max: #repete o raciocinio 
#        saida = "Ian"
#        max = n[2]
#    if n[0] == n[1] or n[1] == n[2] or n[2] == n[0]:
#        saida = "Empate"
#    print(saida)
#
#n=input().split()
#amigos(n)

def comp(a, k):
    if a>k:
        return 1
    elif a<k:
        return 2
    else:
        return 3

o, b, i = map(float, input().split())

if comp(o, b) == 2 and comp(o, i) == 2:
    print('Otavio')
elif comp(b, o)  == 2 and comp(b, i)  == 2:
    print('Bruno')
elif comp(i, o)  == 2 and comp(i, b)  == 2:
    print('Ian')
else:
    print('Empate')