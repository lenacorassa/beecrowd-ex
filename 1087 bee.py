n1=1
while n1!=0:
    n1, m1, n2, m2 = map(int, input().split())
    if n1 != 0 :
       if n1 == n2 and m1 == m2:
           print (0)
       elif n1 == n2 or m1 == m2 or abs(n1-n2) == abs(m1-m2):
           print(1)
       else:
           print(2)
           
