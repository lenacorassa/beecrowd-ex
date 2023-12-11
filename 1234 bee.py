while True:
    try:
        
        linha = input()
        nova_linha = ""

        upper = True

        for i in linha:
            if i == ' ':
                nova_linha += ' '
                continue

            if upper:
                nova_linha += i.upper()
                upper = False

            else:
                nova_linha += i.lower()
                upper = True

        print(nova_linha)

    except EOFError:
        break