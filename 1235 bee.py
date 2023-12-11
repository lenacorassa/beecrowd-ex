#n = int(input())

#while(n > 0):
    #n -= 1
    #c = input()
   # m = int(len(c)/2) -1
   # saida = c[m::-1] + c[len(c)-1:m:-1]
  #  print(saida)

n = int(input())

for _ in range(n):
    frase = input()

    part1 = frase[:len(frase)//2]
    part2 = frase[len(frase)//2:]

    print(part1[::-1] + part2[::-1])