a,b,c=map(float,input().split())
if (a<b+c and b<a+c and c<b+a):
    print("Perimetro = %0.1f"%(a+b+c))
else:
    print("Area = %0.1f"%(((a+b)*c)/2))