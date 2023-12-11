even = []
odd = []

for i in range(15):
    v = int(input())

    if (v % 2 == 0):
        even.append(v)
    else:
        odd.append(v)

    if (len(even) == 5):
        cont = 0
        for v in even:
            print(f"par[{cont}] = {v}")
            cont += 1
        even = []

    if (len(odd) == 5):
        cont = 0
        for v in odd:
            print(f"impar[{cont}] = {v}")
            cont += 1
        odd = []

if (len(odd) > 0):
    cont = 0

    for v in odd:
        print(f"impar[{cont}] = {v}")
        cont += 1

if (len(even) > 0):
    cont = 0

    for v in even:
        print(f"par[{cont}] = {v}")
        cont += 1