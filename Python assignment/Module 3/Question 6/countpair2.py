L1=list(map(int,input()))
L2=list(map(int,input()))
sum=int(input())
i=0
count=0
value=0
while (value<(len(L1)-1)):

   if(L1[value]+L2[i])==sum:
      if(value==i):i=i+1
      print("L1[{0}]+L2[{1}]={2}".format(value,i,sum))
      count=count+1


   if(i==(len(L1)-1)):
        value=value+1
        i=value+1
   else: i=i+1
if(count!=0): print(count)
else: 
    print("false")
