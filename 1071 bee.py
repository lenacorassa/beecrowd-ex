x=int(input())
y=int(input())
ans=0
for n in range((y+1),x):
    if (n%2!=0):
        ans+=n
print(ans)