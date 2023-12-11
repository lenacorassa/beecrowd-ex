n = int(input())

while n:
    n -= 1
    rotina = input()
    ref1 = input()
    ref2 = input()
    ref2 += ref1
    for i in range(len(ref2)):
        if ref2[i] not in rotina:
            rotina = 'CHEATER'
            break
        else:
            rotina = rotina.replace(ref2[i], '')

    if rotina != 'CHEATER':
        rotina = ''.join(sorted(rotina))
    print(rotina)