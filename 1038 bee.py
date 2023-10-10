Item, Quantidade = map(int,input().split())
if Item==1:
    preco = Quantidade*4
elif Item==2:
    preco = Quantidade*4.5
elif Item==3:
    preco = Quantidade*5
elif Item==4:
    preco = Quantidade*2
elif Item==5:
    preco = Quantidade*1.5

print(f"Total: R${preco:.2f}")

