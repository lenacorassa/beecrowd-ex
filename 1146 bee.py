n = int(input())

while n != 0:
  
    for i in range(1, n+1):
        if i != n:
            print(i, end=' ')
        else:
            print(i)
            
    n = int(input())