import math

v,p =map(int, input().split())

total = v * p
pr = 10.0
rsp = []
for i in range(1, 10):
  placas = (total * p)/100.0
  rsp.append(str(math.ceil(placas)))
  pr += 10.0
saida = ('{rsp}')
print(saida)