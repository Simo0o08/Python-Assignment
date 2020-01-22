square=[[4,9,2],[3,5,7],[8,1,6]]
n=len(square)

diag1=0
diag2=0

for i in range(n):
    diag1=diag1+square[i][i]
    diag2=diag2+square[i][n-i-1]



for i in range(n):
   colSum=0
   rowSum=0
   for j in range(n):
      colSum=colSum+square[j][i]
      rowSum=rowSum+square[i][j]
   if(colSum != rowSum != diag1 != daig2):
         print("NO")
         exit()



if(diag1==diag2==colSum==rowSum):
   print("YES, it is a magic square")