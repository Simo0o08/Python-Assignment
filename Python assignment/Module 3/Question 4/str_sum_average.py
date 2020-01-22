str=input().split(' ')
t=[int(str[i]) for i in range(2,len(str),3)]
print("sum =", sum(t),"percentage =",round(sum(t)/len(t),2),"%")
