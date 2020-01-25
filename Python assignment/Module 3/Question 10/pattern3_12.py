#Diamond star pattern

level=int(input())
i=0
p=level//2
k=1
str=1
j=level//2
while(i<(level//2+1)):
   j=p
   while(j>0):
     print(" ",end=" ")
     j=j-1
   k=1 
   while(k<=str):
     print("@",end=" ")
     k=k+1
   str=str+2   
   print()
   p=p-1
   i=i+1

i=0
p=1
str=str-4
while(i<(level//2)):
   j=1
   while(j<=p):
     print(" ",end=" ")
     j=j+1
   k=1 
   while(k<=str):
     print("@",end=" ")
     k=k+1
   str=str-2 
   p=p+1
   i=i+1
   print()
   
   

