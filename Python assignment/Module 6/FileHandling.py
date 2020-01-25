f=open('Sim.txt',"r")
#f.write(b"hy")
line=f.readline()

#print(line)
while(line !=''):

   amt=float(line)
   print(amt)
   line=f.readline().rstrip('\n')
  
f.close()


