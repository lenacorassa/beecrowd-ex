n = int(input())
a = [int(x) for x in input().split()]

while len(a) != 1:
   x = []

   for i in range(len(a)-1):
      if a[i] == a[i+1]: 
         x.append(1)
      else: 
         x.append(-1)
   a = x[:]

if x[0] == -1: 
   print('branca')
else: 
   print('preta')