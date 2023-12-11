n = 0
g = a = d = 0

while n != 4:
    n = int(input())

    if n == 1:
        a += 1
    elif n == 2:
        g += 1 
    elif n == 3:
        d += 1

print(f'''MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}''')