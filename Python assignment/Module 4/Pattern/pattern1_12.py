#Left Arrow Star Pattern

n=int(input())
k=n
i=n
r=0
while(r<n):
  k=i
  while(k>=1):
   print("*",end=" ")
   k=k-1
  i=i-1
  print()
  k=i
  r=r+1
r=0
i=3
while(r<n-1):
  k=i
  while(k>1):
   print("*",end=" ")
   k=k-1
  i=i+1
  print()
  k=i
  r=r+1
 

