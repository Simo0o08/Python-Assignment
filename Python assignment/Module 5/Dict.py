#nested dictionary...............
people={1:{'name':'john','age':78,'sex':'Male'},2:{'name':'marry','age':68,'sex':'Female'}}
print(people)

print(people[1]['name'])
print(people[2]['sex'])


#Append...................
people[3]={}
people[3]['name']='Simran'
people[3]['age']=22
people[3]['sex']='female'
people[3]['married']='NO'

people[4]={'name':'Piru','age':39,'sex':'Female'}

#DEL.............

del people[3]['married']
del people[4]
print(people)
print(people[3])

#Traverse.............

for p_id,p_info in people.items():
   print("Person id",p_id)
   for key in p_info:
      print( key, " :",p_info[key])