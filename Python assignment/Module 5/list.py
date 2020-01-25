#Nested list

matrix=[[j for j in range(5)] for i in range(5)]
print(matrix)

matrix1=[]
for i in range(5):
  matrix1.append([])
  for j in range(5):
     matrix1[i].append(j)
print(matrix1)



#Flatter Matrix(join all sublists into one list)...........

flatter_matrix=[]
for i in matrix:
   for j in i:
    if j<4:
     flatter_matrix.append(j)

print(flatter_matrix)

# .................OR.............

f=[]
for i in matrix:
   f.extend(i)
print(f)


# Flatter upto fixed length
planet=[["cdretfrgt","qwefrgthyuj"],["swdefrt","ds","s"]]
f=[i for sublist in planet for i in sublist if len(i)<6]
print(f)
