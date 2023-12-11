n=int(input())
for _ in range (n):
    n1=int(input())
    cont=True
    lingua=""

    for i in range (n1):
        if not lingua:
            lingua=input()
        else:
            if lingua != input():
                cont=False
    if cont:
        print (lingua) 
    else:
        print("ingles")       