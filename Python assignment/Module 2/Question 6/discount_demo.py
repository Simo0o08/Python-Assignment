NOP=int(input())
discount=0
if(NOP>=10 and NOP<=19):
  discount=10/100
else:
  if(NOP>=20 and NOP<=49):
     discount=20/100
  else:
     if(NOP>=50 and NOP<=99):
         discount=30/100
     else:
         if(NOP>=100):
              discount=40/100

discount=discount*99*NOP
amount=NOP*99-discount
if(NOP>9):
 print("Discount=",discount)

print("amount=",amount)