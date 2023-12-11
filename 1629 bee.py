while True:
    n = int(input())
    if n == 0:
        break
    while n > 0:
        n -= 1
        um = 0
        n0 = 0
        linha = input()
        for i in range(len(linha)):
            if i % 2 == 0:
                n0 += int(linha[i])
            else:
                um += int(linha[i])
        ans = 0
        while (n0):
            ans += (n0 % 10)
            n0 = int(n0/10)
        while (um):
            ans += (um % 10)
            um = int(um/10)
        print(ans)