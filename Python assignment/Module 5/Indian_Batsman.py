Indian_batsman={"Batsman":{"ROhit_SHarma":{"Matches":45,'Runs':45,"Average":47.4,'Highest Score': 264},
"Virat_Kohli":{"Matches":67,'Runs':100,"Average":50.4,'Highest Score': 2564},
"Sachin":{"Matches":655,'Runs':455,"Average":474.4,'Highest Score': 2654}
}}

#print(Indian_batsman['Batsman']['Virat_Kohli']['Runs'])
Indian_batsman["Baller"]={}

a=[]
[a.append(t) for i,j in Indian_batsman.items() for k,f in j.items() for p,t in f.items() if(p=="Highest Score")]
l=max(a)

a=[]
[a.append((str(t),k)) for i,j in Indian_batsman.items() for k,f in j.items() for p,t in f.items() if(p=="Highest Score")]
a=max(a)
print("Highest score :",a[0]," , Name:" , a[1])


'''
a=[]
for i,j in Indian_batsman.items():
    for k,f in j.items():
      for p,t in f.items():
       if(p=="Highest Score"):
          a.append((str(t),k))
a=max(a)
print("Highest score :",a[0]," , Name:" , a[1])
print("Highest score :",a[1])
'''

#print(Indian_batsman)