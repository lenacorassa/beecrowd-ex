a = b = 0 

while a < 2:
    n = float(input())

    if 0 <= n <= 10:
        b += n
        a += 1 
    else:
        print('nota invalida')

print(f'media = {b/2}')