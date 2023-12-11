while True:
    try:
        x,y,m=map(int, input().split())

        for i in range(0,m):
            x1,y1=map(int, input().split())
            if (x1<=x and y1<=y) or (x1<=y and y1<=x):
                print("Sim")
            else:
                print("Nao")
            

    except EOFError:
        break