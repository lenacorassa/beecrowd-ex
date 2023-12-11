# l = int(input())
# opera = input()
   

# m=[]
# for i in range(12):
#     m.append([])

# for i in range(12):
#     for j in range(12):
#         x = float(input())
#         m[i].append(x)
        

# if opera == 'S':
#     soma = 0
#     for k in m[l]:
#         soma = soma + k
#     print(soma)
# if opera == 'M':
#     med = 0
#     soma = 0
#     for k in m[l]:
#         soma = soma + k
#     med= soma/12
#     print(med)

line = int(input())
n= input()
c= 0

for i in range(12):

    for j in range(12):
        v = float(input())
        
        if (i == line):
            c += v

if (n == 'S'):
    print("%.1f" % c)
else:
    print("%.1f" % (c / 12.0))