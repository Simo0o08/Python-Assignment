n=int(input())
i=0
ans=0
lis=[]
while(i<5):
 z=n%10
 z=z+1
 lis.append(z)
 n=n//10
 i=i+1
p=list(reversed(lis))
for i in range(len(p)):
 print(p[i],end=" ")



 