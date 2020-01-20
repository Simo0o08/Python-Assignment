n=int(input())
if(n==0):
 print("green")
else:
 if((n>=1 and n<=10) or (n>=19 and n<=28)):
   if(n%2==0):
     print("black")
   else:
     print("red")
 else:
     if((n>=11 and n<=18) or (n>=29 and n<=36)):
        if(n%2==0):
           print("red")
        else:
           print("black")
     else:
           print("error")

