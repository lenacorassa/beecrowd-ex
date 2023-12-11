n = int(input())

for _ in range (n):
    
    linha=input().split()
    new_line=""

    for i in linha:
        if i!=' ':
            new_line+=i[0]

    print(new_line)


