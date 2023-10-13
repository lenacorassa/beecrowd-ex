salary=float(input())
if(0<salary<=2000):
    print("Isento")
elif(2000<salary<=3000):
    txisento= (salary-2000)
    tx0= (txisento*8)/100
    print("R$ %.2f"%tx0)
elif(3000<salary<=4500):
    txisento= (salary-2000)
    t1=txisento-1000
    tx1=(1000*8)/100
    tx2= (t1*18)/100
    print("R$ %.2f"%(tx1+tx2))
else:
    txisento= (salary-2000)
    t1= txisento-1000
    t2=t1-1500
    tx1=(1000*8)/100
    tx2=(1500*18)/100
    tx= (t2*28)/100
    print("R$ %.2f" %(tx+tx1+tx2))