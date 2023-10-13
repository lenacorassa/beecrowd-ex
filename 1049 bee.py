nome1 = input()
nome2 = input()
nome3 = input()
if nome1=='vertebrado':
    if nome2 == 'ave':
        if nome3 == 'carnivoro':
            print("aguia")
        elif nome3 == 'onivoro':
            print("pombo")
    if nome2 == 'mamifero':
        if nome3 == 'onivoro':
             print("homem")
        elif nome3 == 'herbivoro':
            print("vaca")
if nome1 == 'invertebrado':
    if nome2 == 'inseto':
        if nome3 == 'hematofago':
            print("pulga")
        elif nome3 == 'herbivoro':
            print("lagarta")
    if nome2 == 'anelideo':
        if nome3 == 'hematofago':
            print("sanguessuga")
        elif nome3 == 'onivoro':
            print("minhoca")