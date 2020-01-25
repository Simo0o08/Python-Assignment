B={'fruit':[{"Name":'apple','botanicalName':'Malus Domestica','MajorProducers':['China','US','Turkey'],'Nutrition':{'Carbs':'6','fat':'6','protien':'66'}},
{'Name':'orange','botanicalName':'popo','MajorProducers':['China','Pakistan','America'],'Nutrition':{'Carbs':'6','fat':'6','protien':'89'}},
{'Name':'banana','botanicalName':'jpjpo','MajorProducers':['London','Pakistan','America'],'Nutrition':{'Carbs':'3','fat':'6','protien':'78'}}
]}
#print((B['fruit'][0]['Name']))


#Fruit with Highest protien value
a=[]
for i in range(len(B['fruit'])):
  #print(B['fruit'][i]['Nutrition']['protien'])
  a.append((B['fruit'][i]['Nutrition']['protien'],(B['fruit'][i]['Name'])))
a=max(a)
print("Max Protien :",a[0],", Name of fruit:" , a[1])


#Fruit with Highest protien value in china
b=[]
for i in range(len(B['fruit'])):  
  #print(B['fruit'][i]['MajorProducers'])
  for j in range(3):
    if(B['fruit'][i]['MajorProducers'][j]=='China'):
      b.append((B['fruit'][i]['Nutrition']['protien'],(B['fruit'][i]['Name'])))
b=max(b)
print("Max Protien in china :",b[0],", Name of fruit:" , b[1])


