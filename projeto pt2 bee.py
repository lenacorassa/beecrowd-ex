def verifica_texto(texto):
    erros = []

    # Função para adicionar erro à lista
    def adiciona_erro(tipo, posicao):
        erros.append((tipo, posicao))

    # Verifica espaços em branco consecutivos
    if '  ' in texto:
        adiciona_erro('ESPACO EM BRANCO', [i for i, c in enumerate(texto) if texto[i:i+2] == '  '])

    # Verifica palavras informais
    for i, palavra in enumerate(texto.split()):
        if any(c.isdigit() for c in palavra) and not any(c.isalpha() for c in palavra):
            for j, char in enumerate(palavra):
                if char.isdigit():
                    adiciona_erro('INFORMAL', i + j + 1)

    # Verifica letra maiúscula após ponto final
    if len(texto) > 1 and texto[0].islower():
        adiciona_erro('MAIUSCULA', [1])

    for i in range(1, len(texto) - 1):
        if texto[i - 1] == '.' and texto[i].islower():
            adiciona_erro('MAIUSCULA', [i + 1])

    # Verifica letra minúscula após espaço em branco
    for i in range(1, len(texto)):
        if texto[i - 1] == ' ' and texto[i].isupper():
            adiciona_erro('MINUSCULA', [i])

    # Verifica símbolos de pontuação
    pontuacoes = {',', '.'}
    for i, char in enumerate(texto):
        if char in pontuacoes:
            if i == 0 or i == len(texto) - 1 or texto[i-1] == ' ' or texto[i+1] == ' ':
                adiciona_erro('PONTUACAO', [i])

    # Imprime resultados
    if not erros:
        print('SIM')
    else:
        print('NAO')
        for tipo, posicoes in erros:
            print(tipo)
            print(*posicoes)

# Testando com o exemplo fornecido
texto_entrada = "a ascens4o de Napole4o desde suas origens humildes   at3 chegar ao poder , eh uma narrativa que parece coisa de f1lme. Sua capacidade de transformar desafios em oportunidades eh um exemplo."
verifica_texto(texto_entrada)

texto_entrada = "Napoleao era um hOmem muito ambicioso, mas lutou ate quando foi possivel resistir. depois ficou exilado na ilha de elba. No entanto, ele retornou brevemente em 1815, conhecido como o 'Periodo dos Cem Dias', antes de ser derrotado em waterloo e exilado definiti.vamente para uma ilha misteriosa. Napoleao era 1 grande estrategista, tambem foi um patrono das artes e das ciencias."
verifica_texto(texto_entrada)

texto_entrada = "Surgida em 1976, a banda foi um quinteto formado por ric ocasek, benjamin orr, david robinson, greg hawkes e elliot easton. A banda foi formada em boston, massachusetts, cidade estadunidense considerada de expressiva cena de rock alternativo."
verifica_texto(texto_entrada)

texto_entrada = "No inicio do seculo 19, napoleao emergiu como uma figura iconica na Europa. Suas campanhas militares, marcadas por estrategias ousadas, estabeleceram eLe como um dos maiores com4ndantes da historia. seu legado influenciou as taticas militares por decadas."
verifica_texto(texto_entrada)
