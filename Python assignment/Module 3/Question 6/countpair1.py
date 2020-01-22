L=list(map(int,input()))
sum=int(input())
i=0
count=0
value=0
while (value<(len(L)-1)):

   if(L[value]+L[i])==sum:
      if(value==i):i=i+1
      print("L[{0}]+L[{1}]={2}".format(value,i,sum))
      count=count+1

   if(i==(len(L)-1)):
        value=value+1
        i=value+1
   else: i=i+1
if(count!=0): print(count)
else: 
    print("false")
