# def corrija(texto):
#     erros = []

#     # Função para adicionar erro à lista
#     def ache_erro(tipo, posicao):
#         erros.append((tipo, posicao))

#     # Verifica espaços em branco consecutivos
#     if '  ' in texto:
#         ache_erro('ESPACO EM BRANCO', [i for i, c in enumerate(texto) if texto[i:i+2] == '  '])

#     # Verifica palavras informais
#     for i, palavra in enumerate(texto.split()):
#         if any(c.isdigit() for c in palavra) and not any(c.isalpha() for c in palavra):
#             for j, char in enumerate(palavra):
#                 if char.isdigit():
#                     ache_erro('INFORMAL', i + j + 1)

#     # Verifica letra maiúscula após ponto final
#     if len(texto) > 1 and texto[0].islower():
#         ache_erro('MAIUSCULA', [1])

#     for i in range(1, len(texto) - 1):
#         if texto[i - 1] == '.' and texto[i].islower():
#             ache_erro('MAIUSCULA', [i + 1])

#     # Verifica letra minúscula após espaço em branco
#     for i in range(1, len(texto)):
#         if texto[i - 1] == ' ' and texto[i].isupper():
#             ache_erro('MINUSCULA', [i])

#     # Verifica símbolos de pontuação
#     pontuacoes = {',', '.'}
#     for i, char in enumerate(texto):
#         if char in pontuacoes:
#             if i == 0 or i == len(texto) - 1 or texto[i-1] == ' ' or texto[i+1] == ' ':
#                 ache_erro('PONTUACAO', [i])

#     # Imprime resultados
#     if not erros:
#         print('SIM')
#     else:
#         print('NAO')
#         for tipo, posicoes in erros:
#             print(tipo)
#             print(*posicoes)



# def verifica_espacos(texto):
#     posicao_erro = []

#     for i in range(len(texto) - 1):
#         if texto[i] == ' ' and texto[i + 1] == ' ':
#             posicao_erro = i
#             break

#     if posicao_erro is not None:
#         print(f'SIM\nErro na posição: {posicao_erro}')
#     else:
#         print('NÃO')

# # Exemplo de uso:
# texto_exemplo = "Este  é  um exemplo  com  espaços  em  excesso."
# verifica_espacos(texto_exemplo)

def verifica_espacos(texto):
    erro1 = []

    for i in range(len(texto) - 1):
        if texto[i] == ' ' and texto[i + 1] == ' ':
            erro1.append(i+1)
    return erro1

def erro_informal(texto):
    erro2=[]
    count=0
    for i in range(len(texto)):
        item=texto[i]
        if item != ' ':
            count+=1
        if item == ' ':
            count=0
        if count==1:
            if item.isalpha():
                flag='letra'
            else:
                flag='numero'
        if count>1:
            if flag=='letra':
                if not item.isalpha():
                    erro2.append(i)
    return erro2

def erro_maiuscula(texto):
    erro3=[]
    


def erro_minuscula(texto):
    erro4=[]
    flag='naoMaius'
    if texto[0].islower():
        erro4.append(0)
    for i in range(len(texto)-1):
        item0=texto[i]
        item1=texto[i+1]
        if item0=='.' and item1==' ':
            flag='proxLetraEhMaius'
        if flag=='proxLetraEhMaius' and item0.islower():
            erro4.append(i)
        if item0.isalpha() or item0.isdigit():
            flag='naoMaius'
    return erro4



ex='o arR0z  . cust4 45'
errosEspaco = verifica_espacos(ex)
erroInformal = erro_informal(ex)
erroMinuscula = erro_minuscula(ex)



erros = {}

erros['espaco_em_branco'] = errosEspaco
erros['erro_informal'] = erroInformal
erros['erro_minuscula'] = erroMinuscula
print(erros)