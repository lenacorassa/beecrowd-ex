#while True:
#  try: print(int(0.99+(int(input())*0.01)))
#  except: break
while True:
    try:
        ano=int(input())
        sec=int(ano/100+0.99)
        print(sec)
    except: break