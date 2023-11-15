E,F,C= map(int, input().split())
total=E+F

while total//C>0:
    novo_refri=(total//C)
    novo_refri1=novo_refri+(novo_refri//C)
    print(novo_refri1)
    