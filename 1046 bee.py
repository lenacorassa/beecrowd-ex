hora1, hora2 = map(int, input().split())
horafinal = hora2*60 - hora1*60
if horafinal<=0:
    horafinal += 24*60
print (f"O JOGO DUROU {horafinal//60} HORA(S)")