#Hollow pyramid star pattern


row=int(input())
i=0
p=row
k=1
str=1
j=row
while(i<row):
  j=p
  while(j>0):
     print(" ",end="")
     j=j-1
  p=p-1
  for j in range(i*2+1):  
     if((j==0) or (j==(i*2))):
        print("*",end="")
     else:
        print(" ",end='')
  print()
  i=i+1
i=0
for i in range(row+1):
  print("*",end=" ")
 
  