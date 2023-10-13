dia1 = int(input().split()[1])
hora, minuto, segundo = map(int, input().split(" : "))
dia2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(" : "))

segundo = dia1*24*60*60+hora*60*60+minuto*60+segundo
s2 = dia2*24*60*60+h2*60*60+m2*60+s2

tempof = s2-segundo

if tempof<=0:
    tempof=tempof+24*60*60

print(f'''{tempof//60//60//24} dia(s)
{tempof//60//60%24} hora(s)
{tempof//60%60} minuto(s)
{tempof%60} segundo(s)''')
