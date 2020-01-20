n=int(input())
sum=0
i=0
while(i<5):
   sum=sum+(n%10)
   n=n//10
   i=i+1
print(sum)