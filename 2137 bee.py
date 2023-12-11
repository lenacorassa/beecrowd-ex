while True:
    try:
        n = int(input())
        x = []
        while(n > 0):
            n -= 1
            x.append(input())
        x.sort()
        
        for n in x:
            print(n)
        
    except EOFError:
        break