n,m=map(int,input().split(' '))
s=list(map(int,input().split(' ')))
max=0
for i in range(n):
   if(i+m>n-1):
     k=sum(s[i:])+sum(s[0:i+m-n])
     #print(k,s[i+m-n])
   else: 
     k=sum(s[i:i+m]) 
     #print(k,s[i],s[m+i])
   if(k>max):
     max=k
     continue

print(max)


'''

m,n=map(int,input().split(' '))
L=list(map(int,input().split(' ')))
i=0
p=[]
while(i<m):
   prev=i-1
   next=i+1   
   num1=L[i]
   if(prev<0):
    num2=L[-1] 
   else: num2=L[prev]
   if(next==m): 
     num3=L[0]
   else:
     num3=L[next]
   sum=num1+num2+num3
   p.append(sum)
   i=i+1
print(max(p))

    
'''