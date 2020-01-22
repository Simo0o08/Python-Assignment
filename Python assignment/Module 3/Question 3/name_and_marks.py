s=input()
c=list(s.split(','))
for i in range(1,len(c)):
  c[i]=int(c[i])
print("Robert obtained", sum(c[1:6]) , "marks out of 500 in theory and ", sum(c[6:8]),"marks out of 30 in practical and successfully passed the exam with",round((sum(c[1:]))*100/650,2), "in aggregate. Many congratulations to Robert.")

