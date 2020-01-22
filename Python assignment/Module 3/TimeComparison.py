import datetime
a = datetime.datetime.now()
'''odd_square=[]
for x in range(1,11):
   if(x%2==1):
     odd_square.append(x**2)
print(odd_square)
'''

odd_square=[x**2 for x in range(1,11) if x%2==1]
print(odd_square)
b = datetime.datetime.now()
c=b-a
print(c)
